from app.database.repositories.task_repository import TaskRepository
from app.decision.scoring import TaskScorer


class Planner:

    def __init__(self):

        self.repository = TaskRepository()
        self.scorer = TaskScorer()

    def suggest(self, state):

        tasks = self.repository.get_pending_tasks()

        if not tasks:
            print("\n🐾 Não existem tarefas.")
            return

        scored = []

        for task in tasks:

            points = self.scorer.score(task, state)

            scored.append((points, task))

        scored.sort(reverse=True, key=lambda item: item[0])

        print("\n🐾 Sugestões")

        for points, task in scored[:3]:

            print(f"{points:3} pts | {task.title}")
