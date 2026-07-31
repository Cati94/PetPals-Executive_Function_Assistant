from app.database.repositories.project_repository import ProjectRepository


class ProjectService:

    def __init__(self):

        self.repository = ProjectRepository()

    def create_project(
        self,
        name,
        description="",
    ):

        return self.repository.create(
            name,
            description,
        )

    def list_projects(self):

        return self.repository.list_all()
