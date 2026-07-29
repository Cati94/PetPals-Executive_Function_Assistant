from app.database.database import initialize_database
from app.database.models import Priority, EnergyLevel
from app.services.task_service import TaskService

initialize_database()

service = TaskService()

service.create_task(
    title="Continuar PetPals",
    description="Criar o TaskService",
    priority=Priority.HIGH,
    energy_level=EnergyLevel.MEDIUM,
    estimated_minutes=45,
)

for task in service.list_tasks():
    print(task.id, task.title)
