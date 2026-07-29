"""
PetPals
Personal AI Executive Assistant

Ponto de entrada da aplicação.
"""

from app.core.startup import startup
from app.ui.menu import Menu


def main() -> None:
    """Executa o arranque do PetPals."""
    startup()


if __name__ == "__main__":
    main()
    
def main():
    startup()

    menu = Menu()
    menu.show()


if __name__ == "__main__":
    main()