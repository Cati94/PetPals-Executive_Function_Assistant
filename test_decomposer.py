from app.decomposer.decomposer import TaskDecomposer

decomposer = TaskDecomposer()

steps = decomposer.decompose("Programar PetPals")

for index, step in enumerate(steps, start=1):
    print(f"{index}. {step}")
