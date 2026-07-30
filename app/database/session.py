"""
Gestão de sessões da base de dados.
"""

from sqlalchemy.orm import sessionmaker

from app.database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_session():
    """Cria uma nova sessão da base de dados."""
    return SessionLocal()
