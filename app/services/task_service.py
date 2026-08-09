"""
Serviço responsável pela gestão de tarefas.
"""

from app.database.models import EnergyLevel, Priority, Task
from app.database.repositories.task_repository import TaskRepository


class TaskService:
    """Lógica de negócio das tarefas."""

    def __init__(self):
        self.repository = TaskRepository()

    def create_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        energy_level: EnergyLevel = EnergyLevel.MEDIUM,
        estimated_minutes: int = 30,
        context: str = "general",
        project=None,
    ) -> Task:
        """Cria uma nova tarefa."""

        return self.repository.create(
            title=title,
            description=description,
            priority=priority,
            energy_level=energy_level,
            estimated_minutes=estimated_minutes,
            context=context,
            project=project,
        )

    def list_tasks(self) -> list[Task]:
        """Lista todas as tarefas."""

        return self.repository.list_all()

    def complete_task(self, task_id: int) -> Task | None:
        """Marca uma tarefa como concluída."""

        return self.repository.complete(task_id)
