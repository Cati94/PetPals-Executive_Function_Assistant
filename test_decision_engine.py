from app.executive.decision_engine import DecisionEngine
from app.user.user_state import (
    UserState,
    Energy,
    Focus,
    Mood,
)

engine = DecisionEngine()

state = UserState(
    energy=Energy.VERY_LOW,
    focus=Focus.LOW,
    mood=Mood.BAD,
)

context = engine.evaluate(state)

print("Task size:", context.task_size)
print("Max tasks:", context.max_tasks)
print("Breaks:", context.breaks)
print("Load:", context.cognitive_load)
