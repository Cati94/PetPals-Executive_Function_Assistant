"""
Modelos da base de dados do PetPals.
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.database import Base


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class EnergyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class SystemInfo(Base):
    __tablename__ = "system_info"

    id: Mapped[int] = mapped_column(primary_key=True)

    key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )

    value: Mapped[str] = mapped_column(
        String(255),
    )


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(1000),
        default="",
    )

    priority: Mapped[Priority] = mapped_column(
        SqlEnum(Priority),
        default=Priority.MEDIUM,
    )

    energy_level: Mapped[EnergyLevel] = mapped_column(
        SqlEnum(EnergyLevel),
        default=EnergyLevel.MEDIUM,
    )

    estimated_minutes: Mapped[int] = mapped_column(
        Integer,
        default=30,
    )

    context: Mapped[str] = mapped_column(
        String(100),
        default="general",
    )

    status: Mapped[TaskStatus] = mapped_column(
        SqlEnum(TaskStatus),
        default=TaskStatus.TODO,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
