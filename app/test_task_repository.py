from app.database.database import initialize_database
from app.database.models import (
    Task,
    Priority,
    EnergyLevel,
)
from app.database.repositories.task_repository import TaskRepository

initialize_database()

repo = TaskRepository()

task = Task(
    title="Estudar SQLAlchemy",
    description="Aprender Repository Pattern",
    priority=Priority.HIGH,
    energy_level=EnergyLevel.MEDIUM,
    estimated_minutes=60,
)

repo.create(task)

print("ID:", task.id)

tasks = repo.list_all()

for item in tasks:
    print(item.id, item.title)