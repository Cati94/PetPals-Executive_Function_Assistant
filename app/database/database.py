"""
Configuração da base de dados do PetPals.
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


class Base(DeclarativeBase):
    """Classe base para todos os modelos."""

    pass


engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
)


def initialize_database() -> None:
    """Inicializa a base de dados."""

    Path("data/database").mkdir(parents=True, exist_ok=True)

    # Importar modelos apenas aqui

    Base.metadata.create_all(bind=engine)
