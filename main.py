"""
PetPals
Personal AI Executive Assistant

Ponto de entrada da aplicação.
"""

from app.core.startup import startup
from app.ui.menu import Menu
from app.user.user_service import UserService
from app.planner.planner import Planner


def main() -> None:
    """Executa o arranque do PetPals."""

    startup()

    user = UserService()
    state = user.ask_daily_status()

    planner = Planner()
    planner.suggest(state)

    print()
    print("Estado atual:")
    print(state)

    menu = Menu()
    menu.show()


if __name__ == "__main__":
    main()
