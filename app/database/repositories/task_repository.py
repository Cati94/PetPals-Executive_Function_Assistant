"""
Repositório das tarefas.
"""

from sqlalchemy import select

from app.database.models import Task
from app.database.session import get_session


class TaskRepository:
    """Operações sobre a tabela Task."""

    def create(self, task: Task) -> Task:
        """Guarda uma nova tarefa."""

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