"""
Modelos da base de dados do PetPals.
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# ==========================================================
# ENUMS
# ==========================================================


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


# ==========================================================
# SYSTEM INFO
# ==========================================================


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


# ==========================================================
# PROJECT
# ==========================================================


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
    )


# ==========================================================
# TASK
# ==========================================================


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

    project_id: Mapped[int | None] = mapped_column(
        ForeignKey("projects.id"),
        nullable=True,
    )

    project = relationship(
        "Project",
        back_populates="tasks",
    )
