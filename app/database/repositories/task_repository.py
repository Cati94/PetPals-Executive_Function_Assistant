from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database.models import (
    EnergyLevel,
    Priority,
    Project,
    Task,
    TaskStatus,
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
        project: Project | None = None,
    ) -> Task:
        """Cria e guarda uma nova tarefa."""

        task = Task(
            title=title,
            description=description,
            priority=priority,
            energy_level=energy_level,
            estimated_minutes=estimated_minutes,
            context=context,
            project=project,
        )

        with get_session() as session:
            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Obtém uma tarefa pelo ID."""

        with get_session() as session:
            stmt = (
                select(Task).options(joinedload(Task.project)).where(Task.id == task_id)
            )

            return session.scalar(stmt)

    def list_all(self) -> list[Task]:
        """Lista todas as tarefas."""

        with get_session() as session:

            stmt = (
                select(Task).options(joinedload(Task.project)).order_by(Task.created_at)
            )

            return list(session.scalars(stmt).all())

    def get_pending_tasks(self) -> list[Task]:
        """Obtém todas as tarefas pendentes."""

        with get_session() as session:

            stmt = (
                select(Task)
                .options(joinedload(Task.project))
                .where(Task.status == TaskStatus.TODO)
                .order_by(Task.priority)
            )

            return list(session.scalars(stmt).all())

    def delete(self, task: Task) -> None:
        """Remove uma tarefa."""

        with get_session() as session:
            session.delete(task)
            session.commit()
