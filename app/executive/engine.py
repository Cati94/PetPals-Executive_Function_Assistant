from app.executive.executive_context import ExecutiveContext
from app.user.user_state import UserState


class ExecutiveFunctionEngine:
    """
    Calcula como o PetPals deve adaptar-se ao utilizador.
    """

    def evaluate(self, state: UserState) -> ExecutiveContext:

        context = ExecutiveContext()

        score = state.energy.value + state.focus.value + state.mood.value

        if score <= 6:

            context.task_size = "small"
            context.max_tasks = 1
            context.breaks = True
            context.cognitive_load = "low"

        elif score <= 10:

            context.task_size = "medium"
            context.max_tasks = 2
            context.breaks = True
            context.cognitive_load = "normal"

        else:

            context.task_size = "large"
            context.max_tasks = 5
            context.breaks = False
            context.cognitive_load = "high"

        return context
