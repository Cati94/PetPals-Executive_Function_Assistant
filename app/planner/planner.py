"""
Planeador de tarefas do PetPals.
"""

from app.database.repositories.task_repository import TaskRepository
from app.executive.decision_engine import DecisionEngine
from app.executive.next_action import NextAction
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
            return None

        context = self.decision_engine.evaluate(state)

        suitable_tasks = [task for task in tasks if self._task_is_suitable(task, state)]

        if not suitable_tasks:
            print("\n🐾 Nenhuma tarefa parece adequada " "para o teu estado atual.")
            return None

        # A primeira tarefa adequada é, por enquanto,
        # a melhor candidata.
        task = suitable_tasks[0]

        action = self._create_next_action(
            task,
            context,
        )

        print(action)

        return action

    def _create_next_action(
        self,
        task,
        context,
    ) -> NextAction:
        """Transforma uma tarefa numa próxima ação."""

        project_name = task.project.name if task.project else "sem projeto"

        reason = (
            f"A tarefa é adequada ao teu estado atual. " f"Projeto: {project_name}."
        )

        confidence = self._calculate_confidence(
            task,
            context,
        )

        return NextAction(
            title=task.title,
            reason=reason,
            estimated_minutes=task.estimated_minutes,
            cognitive_load=context.cognitive_load,
            confidence=confidence,
            total_steps=1,
            current_step=1,
            requires_break=context.breaks,
            show_only_next_step=True,
        )

    def _calculate_confidence(
        self,
        task,
        context,
    ) -> float:
        """Calcula a confiança na recomendação."""

        if context.task_size == "small":
            if task.energy_level.value == "low":
                return 0.95

            return 0.80

        if context.task_size == "medium":
            if task.energy_level.value in (
                "low",
                "medium",
            ):
                return 0.90

            return 0.70

        return 0.85

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
