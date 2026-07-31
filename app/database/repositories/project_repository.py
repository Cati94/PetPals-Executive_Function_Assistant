from sqlalchemy import select

from app.database.models import Project
from app.database.session import get_session


class ProjectRepository:

    def create(
        self,
        name: str,
        description: str = "",
    ) -> Project:

        project = Project(
            name=name,
            description=description,
        )

        with get_session() as session:

            session.add(project)

            session.commit()

            session.refresh(project)

            return project

    def list_all(self):

        with get_session() as session:

            stmt = select(Project)

            return list(session.scalars(stmt).all())
