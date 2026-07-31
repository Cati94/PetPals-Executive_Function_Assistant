from app.projects.project_repository import ProjectRepository


class ProjectService:

    def __init__(self):

        self.repository = ProjectRepository()

    def list_projects(self):

        return self.repository.list_all()
