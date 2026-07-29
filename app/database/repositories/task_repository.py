from sqlalchemy import select

from app.database.models import (
    Task,
    Priority,
    EnergyLevel,
)
from app.database.session import get_session


class TaskRepository:
    """Operações sobre a tabela Task."""

    def create(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        energy_level: EnergyLevel = EnergyLevel.MEDIUM,
        estimated_minutes: int = 30,
        context: str = "general",
    ) -> Task:
        """Cria e guarda uma nova tarefa."""

        task = Task(
            title=title,
            description=description,
            priority=priority,
            energy_level=energy_level,
            estimated_minutes=estimated_minutes,
            context=context,
        )

        with get_session() as session:
            session.add(task)
            session.commit()
            session.refresh(task)

            return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Obtém uma tarefa pelo ID."""

        with get_session() as session:
            stmt = select(Task).where(Task.id == task_id)
            return session.scalar(stmt)

    def list_all(self) -> list[Task]:
        """Lista todas as tarefas."""

        with get_session() as session:
            stmt = select(Task).order_by(Task.created_at)
            return list(session.scalars(stmt).all())

    def delete(self, task: Task) -> None:
        """Remove uma tarefa."""

        with get_session() as session:
            session.delete(task)
            session.commit()