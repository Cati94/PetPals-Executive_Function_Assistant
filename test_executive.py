from app.executive.engine import ExecutiveFunctionEngine
from app.user.user_state import UserState

engine = ExecutiveFunctionEngine()

state = UserState()

context = engine.evaluate(state)

print()

print("Executive Context")

print("----------------")

print(context)
