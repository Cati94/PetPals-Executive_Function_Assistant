from dataclasses import dataclass


@dataclass
class ExecutiveProfile:
    energy: int = 3
    focus: int = 3
    mood: int = 3

    sleep_hours: float = 8.0

    overload: bool = False

    metabolic_energy: int = 3

    available_minutes: int = 60

    interruptions: bool = False

    motivation: int = 3
