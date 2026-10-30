"""Interface web local do PetPals."""

import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
    send_from_directory,
)

from app.core.startup import startup
from app.database.models import (
    EnergyLevel,
    Priority,
    TaskStatus,
)
from app.database.repositories.project_repository import ProjectRepository
from app.database.repositories.task_repository import TaskRepository
from app.decomposer.decomposer import TaskDecomposer
from app.user.user_state import Energy, Focus, Mood, UserState
from app.executive.decision_engine import DecisionEngine


app = Flask(__name__)
app.secret_key = os.environ.get(
    "PETPALS_SECRET_KEY",
    "petpals-local-development-key",
)

task_repository = TaskRepository()
project_repository = ProjectRepository()
decomposer = TaskDecomposer()
decision_engine = DecisionEngine()


@app.get("/service-worker.js")
def service_worker():
    return send_from_directory(
        app.static_folder,
        "service-worker.js",
        mimetype="application/javascript",
    )


def _get_user_state() -> UserState | None:
    """Recupera a avaliação atual guardada na sessão."""
    values = session.get("daily_state")
    if not values:
        return None

    try:
        return UserState(
            energy=Energy(values["energy"]),
            mood=Mood(values["mood"]),
            focus=Focus(values["focus"]),
        )
    except (KeyError, TypeError, ValueError):
        session.pop("daily_state", None)
        return None


def _recommend_task(state: UserState):
    """Escolhe uma tarefa compatível com o estado atual."""
    tasks = task_repository.get_pending_tasks()
    if not tasks:
        return None

    context = decision_engine.evaluate(state)

    suitable = []
    for task in tasks:
        required_energy = task.energy_level.value

        if state.energy.value <= 2:
            matches = required_energy == "low"
        elif state.energy.value == 3:
            matches = required_energy in ("low", "medium")
        else:
            matches = True

        if matches:
            suitable.append(task)

    # Se não houver correspondência exata, não bloquear o utilizador.
    candidates = suitable or tasks

    # Dar prioridade às tarefas já iniciadas.
    candidates.sort(
        key=lambda task: (
            task.status != TaskStatus.IN_PROGRESS,
            task.priority.value != "high",
            task.created_at,
        )
    )

    return candidates[0], context


@app.get("/")
def dashboard():
    all_tasks = task_repository.list_all()
    all_projects = project_repository.list_all()

    pending_tasks = [
        task for task in all_tasks
        if task.status != TaskStatus.DONE
    ]
    completed_count = sum(
        task.status == TaskStatus.DONE
        for task in all_tasks
    )

    state = _get_user_state()
    recommendation = None
    context = None

    if state:
        result = _recommend_task(state)
        if result:
            recommendation, context = result

            # Preparar os passos apenas uma vez, sem substituir
            # passos que já tenham sido guardados.
            if not recommendation.steps:
                steps = decomposer.decompose(recommendation)
                recommendation = task_repository.save_steps(
                    recommendation.id,
                    steps,
                )

    return render_template(
        "index.html",
        tasks=pending_tasks,
        projects=[
            project for project in all_projects if project.active
        ],
        completed_count=completed_count,
        priorities=list(Priority),
        energy_levels=list(EnergyLevel),
        state=state,
        recommendation=recommendation,
        decision_context=context,
    )


@app.post("/assessment")
def assessment():
    """Guarda energia, humor e foco para a recomendação do dia."""
    try:
        energy = Energy(int(request.form["energy"]))
        mood = Mood(int(request.form["mood"]))
        focus = Focus(int(request.form["focus"]))
    except (KeyError, TypeError, ValueError):
        return redirect(url_for("dashboard"))

    session["daily_state"] = {
        "energy": energy.value,
        "mood": mood.value,
        "focus": focus.value,
    }

    return redirect(url_for("dashboard"))


@app.get("/tasks")
def tasks_page():
    all_tasks = task_repository.list_all()
    pending_tasks = [
        task for task in all_tasks
        if task.status != TaskStatus.DONE
    ]
    completed_tasks = [
        task for task in all_tasks
        if task.status == TaskStatus.DONE
    ]

    return render_template(
        "tasks.html",
        tasks=pending_tasks,
        completed_tasks=completed_tasks,
    )


@app.route("/tasks/new", methods=["GET", "POST"])
def new_task():
    projects = [
        project for project in project_repository.list_all()
        if project.active
    ]

    if request.method == "GET":
        return render_template(
            "task_new.html",
            projects=projects,
            priorities=list(Priority),
            energy_levels=list(EnergyLevel),
        )

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    context = request.form.get("context", "general").strip() or "general"

    if not title:
        return render_template(
            "task_new.html",
            projects=projects,
            priorities=list(Priority),
            energy_levels=list(EnergyLevel),
            error="Introduz um título para a tarefa.",
        ), 400

    try:
        priority = Priority(request.form.get("priority", "medium"))
        energy_level = EnergyLevel(
            request.form.get("energy_level", "medium")
        )
        estimated_minutes = int(
            request.form.get("estimated_minutes", "30")
        )

        if not 1 <= estimated_minutes <= 1440:
            raise ValueError

        project_id_raw = request.form.get("project_id", "").strip()
        project = None

        if project_id_raw:
            project_id = int(project_id_raw)
            project = next(
                (
                    item for item in projects
                    if item.id == project_id
                ),
                None,
            )
            if project is None:
                raise ValueError

    except (ValueError, TypeError):
        return render_template(
            "task_new.html",
            projects=projects,
            priorities=list(Priority),
            energy_levels=list(EnergyLevel),
            error="Verifica a prioridade, energia, duração e projeto.",
        ), 400

    task_repository.create(
        title=title,
        description=description,
        priority=priority,
        energy_level=energy_level,
        estimated_minutes=estimated_minutes,
        context=context,
        project=project,
    )

    return redirect(url_for("tasks_page"))


@app.post("/tasks/<int:task_id>/continue")
def continue_task(task_id):
    task = task_repository.get_by_id(task_id)

    if task is None or task.status == TaskStatus.DONE:
        return redirect(url_for("dashboard"))

    if not task.steps:
        task_repository.save_steps(
            task_id,
            decomposer.decompose(task),
        )

    task_repository.advance_step(task_id)
    return redirect(url_for("dashboard"))


@app.post("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    task_repository.complete(task_id)
    return redirect(url_for("dashboard"))


@app.post("/assessment/reset")
def reset_assessment():
    session.pop("daily_state", None)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    startup()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        ssl_context=(
            "certs/petpals.pem",
            "certs/petpals-key.pem",
        ),
    )
