from dataclasses import dataclass


@dataclass
class ExecutiveContext:
    """
    Contexto calculado pelo Executive Engine.
    """

    task_size: str = "normal"
    max_tasks: int = 3
    breaks: bool = False
    cognitive_load: str = "normal"
