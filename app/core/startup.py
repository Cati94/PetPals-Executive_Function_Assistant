"""
Arranque do PetPals.
"""

from app.core.banner import show_banner
from app.core.logger import logger


def startup() -> None:
    """Inicializa o sistema."""

    show_banner()

    logger.info("Loading configuration...")
    logger.success("Configuration loaded")

    logger.success("PetPals is ready.")