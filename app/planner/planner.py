"""
Planeador de tarefas do PetPals.
"""

from app.database.repositories.task_repository import TaskRepository
from app.executive.decision_engine import DecisionEngine
from app.user.user_state import UserState


class Planner:
    """Gera sugestões de tarefas adaptadas ao estado do utilizador."""

    def __init__(self):
        self.repository = TaskRepository()
        self.decision_engine = DecisionEngine()

    def suggest(self, state: UserState):
        """Sugere tarefas de acordo com o estado atual."""

        tasks = self.repository.get_pending_tasks()

        if not tasks:
            print("\n🐾 Não existem tarefas pendentes.")
            return

        context = self.decision_engine.evaluate(state)

        print("\n🐾 Sugestões do PetPals")
        print("-------------------------")

        print(
            f"Tamanho das tarefas: "
            f"{context.task_size}"
        )

        print(
            f"Carga cognitiva: "
            f"{context.cognitive_load}"
        )

        print(
            f"Máximo de tarefas: "
            f"{context.max_tasks}"
        )

        if context.breaks:
            print("⏸️ Recomenda-se fazer pausas.")

        print()

        suitable_tasks = [
            task
            for task in tasks
            if self._task_is_suitable(task, state)
        ]

        if not suitable_tasks:
            print(
                "🐾 Nenhuma tarefa parece adequada "
                "para o teu estado atual."
            )
            return

        limit = min(
            context.max_tasks,
            len(suitable_tasks),
        )

        for index, task in enumerate(
            suitable_tasks[:limit],
            start=1,
        ):
            project_name = (
                task.project.name
                if task.project
                else "Sem projeto"
            )

            print(
                f"{index}. {task.title}"
            )

            print(
                f"   📂 Projeto: {project_name}"
            )

            print(
                f"   ⚡ Energia: "
                f"{task.energy_level.value}"
            )

            print(
                f"   ⏱️ Tempo: "
                f"{task.estimated_minutes} min"
            )

            print()

    def _task_is_suitable(
        self,
        task,
        state: UserState,
    ) -> bool:
        """Determina se a tarefa é adequada ao estado."""

        energy = state.energy.value
        required_energy = task.energy_level.value

        if energy <= 2:
            return required_energy == "low"

        if energy == 3:
            return required_energy in (
                "low",
                "medium",
            )

        return True
