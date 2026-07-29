from app.database.database import initialize_database
from app.database.repositories.task_repository import TaskRepository
from app.database.models import Priority, EnergyLevel

initialize_database()

repo = TaskRepository()

repo.create(
    title="Estudar SQLAlchemy",
    description="Continuar o PetPals",
    priority=Priority.HIGH,
    energy_level=EnergyLevel.MEDIUM,
    estimated_minutes=45,
    context="computer",
)

for task in repo.list_all():
    print(task.id, task.title)