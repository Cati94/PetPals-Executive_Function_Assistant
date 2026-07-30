"""
Sistema de logging do PetPals.
"""

import sys
from pathlib import Path

from loguru import logger

from app.core.config import settings

# Criar diretório de logs
Path("logs").mkdir(exist_ok=True)

# Remover configuração por defeito
logger.remove()

# Terminal
logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    colorize=True,
)

# Ficheiro
logger.add(
    "logs/petpals.log",
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
)

__all__ = ["logger"]
