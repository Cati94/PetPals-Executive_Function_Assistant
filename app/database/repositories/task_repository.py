
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database.models import (
    EnergyLevel,
    Priority,
    Project,
    Task,
    TaskStatus,
)
from app.database.session import get_session


class TaskRepository:
    """Operações sobre a tabela Task."""

    def create(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        energy_level: EnergyLevel = EnergyLevel.MEDIUM,
        estimated_minutes: int = 30,
        context: str = "general",
        project: Project | None = None,
    ) -> Task:
        """Cria e guarda uma nova tarefa."""
        task = Task(
            title=title,
            description=description,
            priority=priority,
            energy_level=energy_level,
            estimated_minutes=estimated_minutes,
            context=context,
            project=project,
        )

        with get_session() as session:
            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Obtém uma tarefa pelo ID."""
        with get_session() as session:
            stmt = (
                select(Task)
                .options(joinedload(Task.project))
                .where(Task.id == task_id)
            )
            return session.scalar(stmt)

    def list_all(self) -> list[Task]:
        """Lista todas as tarefas."""
        with get_session() as session:
            stmt = (
                select(Task)
                .options(joinedload(Task.project))
                .order_by(Task.created_at)
            )
            return list(session.scalars(stmt).unique().all())

    def get_pending_tasks(self) -> list[Task]:
        """Devolve tarefas pendentes ou em curso."""
        with get_session() as session:
            stmt = (
                select(Task)
                .options(joinedload(Task.project))
                .where(
                    Task.status.in_(
                        [TaskStatus.TODO, TaskStatus.IN_PROGRESS]
                    )
                )
                .order_by(Task.priority, Task.created_at)
            )
            return list(session.scalars(stmt).unique().all())

    def complete(self, task_id: int) -> Task | None:
        """Marca uma tarefa como concluída."""
        with get_session() as session:
            stmt = (
                select(Task)
                .options(joinedload(Task.project))
                .where(Task.id == task_id)
            )
            task = session.scalar(stmt)

            if task is None:
                return None

            task.status = TaskStatus.DONE
            task.completed_at = datetime.now()

            session.commit()
            session.refresh(task)
            return task

    def delete(self, task_id: int) -> bool:
        """Remove uma tarefa pelo ID."""
        with get_session() as session:
            task = session.get(Task, task_id)

            if task is None:
                return False

            session.delete(task)
            session.commit()
            return True

    def save_steps(
        self,
        task_id: int,
        steps: list[str],
    ) -> Task | None:
        """Guarda os passos e reinicia o progresso."""
        with get_session() as session:
            task = session.get(Task, task_id)

            if task is None:
                return None

            task.steps = steps
            task.current_step = 0

            if steps and task.status == TaskStatus.TODO:
                task.status = TaskStatus.IN_PROGRESS

            session.commit()
            session.refresh(task)
            return task

    def advance_step(self, task_id: int) -> Task | None:
        """Avança um passo ou conclui a tarefa no último passo."""
        with get_session() as session:
            task = session.get(Task, task_id)

            if task is None or task.status == TaskStatus.DONE:
                return None

            if not task.steps:
                return task

            if task.current_step < len(task.steps) - 1:
                task.current_step += 1
            else:
                task.status = TaskStatus.DONE
                task.completed_at = datetime.now()
                task.current_step = len(task.steps)

            session.commit()
            session.refresh(task)
            return task
