"""
Contexto executivo calculado pelo PetPals.
"""

from dataclasses import dataclass


@dataclass
class ExecutiveContext:
    """Contexto calculado pelo Decision Engine."""

    task_size: str = "normal"
    max_tasks: int = 3
    breaks: bool = False
    cognitive_load: str = "normal"

    recommended_project: object | None = None
    recommended_task: object | None = None

    reason: str = ""
    next_step: str = ""
