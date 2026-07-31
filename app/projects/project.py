from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Project:

    id: int | None = None

    name: str = ""

    description: str = ""

    completed: bool = False

    created_at: datetime | None = None
