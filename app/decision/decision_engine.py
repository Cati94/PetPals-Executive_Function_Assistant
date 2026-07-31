"""
PetPals
Decision Engine

Escolhe a próxima melhor ação para o utilizador.
"""

from app.database.models import Priority
from app.executive.executive_context import ExecutiveContext
from app.executive.next_action import NextAction


class DecisionEngine:
    """Motor de decisão do PetPals."""

    def choose(self, tasks, context: ExecutiveContext) -> NextAction | None:
        """
        Escolhe a melhor tarefa para o estado atual
        do utilizador.
        """

        if not tasks:
            return None

        best_task = None
        best_score = -1

        for task in tasks:

            score = self.calculate_score(task, context)

            if score > best_score:
                best_score = score
                best_task = task

        if best_task is None:
            return None

        reasons = []

        if best_task.priority == Priority.HIGH:
            reasons.append("prioridade elevada")

        elif best_task.priority == Priority.MEDIUM:
            reasons.append("prioridade média")

        if best_task.estimated_minutes <= 20:
            reasons.append("demora pouco tempo")

        if context.task_size == "small":
            reasons.append("adequada ao teu nível de energia")

        return NextAction(
            title=best_task.title,
            reason=", ".join(reasons),
            estimated_minutes=best_task.estimated_minutes,
            cognitive_load=context.cognitive_load,
            confidence=0.95,
        )

    def calculate_score(self, task, context: ExecutiveContext) -> int:
        """
        Calcula a pontuação de uma tarefa.
        """

        score = 0

        # PRIORIDADE

        if task.priority == Priority.HIGH:
            score += 40

        elif task.priority == Priority.MEDIUM:
            score += 20

        else:
            score += 10

        # TEMPO

        if task.estimated_minutes <= 15:
            score += 30

        elif task.estimated_minutes <= 30:
            score += 20

        elif task.estimated_minutes <= 60:
            score += 10

        # ENERGIA

        if context.task_size == "small":

            if task.estimated_minutes <= 20:
                score += 25
            else:
                score -= 20

        elif context.task_size == "medium":

            if task.estimated_minutes <= 45:
                score += 10

        return score
