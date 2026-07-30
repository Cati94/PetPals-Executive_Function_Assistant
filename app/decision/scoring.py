from app.database.models import Priority


class TaskScorer:

    def score(self, task, state):

        score = 0

        if task.priority == Priority.HIGH:
            score += 40

        elif task.priority == Priority.MEDIUM:
            score += 20

        else:
            score += 10

        return score
