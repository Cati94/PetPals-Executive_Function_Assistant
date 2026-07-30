from app.core.banner import show_banner
from app.core.logger import logger
from app.database.database import initialize_database


def startup() -> None:
    show_banner()

    logger.info("Loading configuration...")
    logger.success("Configuration loaded")

    logger.info("Connecting database...")
    initialize_database()
    logger.success("Database connected")

    logger.success("PetPals is ready.")
