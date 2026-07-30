from dataclasses import dataclass
from enum import Enum


class Energy(Enum):
    VERY_LOW = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5


class Mood(Enum):
    VERY_BAD = 1
    BAD = 2
    NORMAL = 3
    GOOD = 4
    EXCELLENT = 5


class Focus(Enum):
    VERY_LOW = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5

@dataclass
class UserState:
    energy: Energy = Energy.NORMAL
    mood: Mood = Mood.NORMAL
    focus: Focus = Focus.NORMAL

    def __str__(self) -> str:
        return (
            f"Energia: {self.energy.name}\n"
            f"Humor: {self.mood.name}\n"
            f"Foco: {self.focus.name}"
        )
