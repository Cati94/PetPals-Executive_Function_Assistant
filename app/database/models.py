"""
Modelos da base de dados.
"""

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.database import Base


class SystemInfo(Base):
    """
    Informações do sistema.
    """

    __tablename__ = "system_info"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )