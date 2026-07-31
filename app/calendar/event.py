from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Event:

    id: int | None = None

    title: str = ""

    start: datetime | None = None

    end: datetime | None = None

    location: str = ""
