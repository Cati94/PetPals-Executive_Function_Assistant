from app.decomposer.decomposer import TaskDecomposer


class FakeTask:
    def __init__(self, title):
        self.title = title


decomposer = TaskDecomposer()

task = FakeTask("Trabalhar nos bugs do FireRisk")

steps = decomposer.decompose(task)

print("\n🐾 Decomposição da tarefa")
print("-------------------------")

for number, step in enumerate(steps, start=1):
    print(f"{number}. {step}")
