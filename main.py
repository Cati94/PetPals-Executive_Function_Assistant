"""
PetPals
Personal AI Executive Assistant

Ponto de entrada da aplicação.
"""

from app.core.startup import startup


def main() -> None:
    """Executa o arranque do PetPals."""
    startup()


if __name__ == "__main__":
    main()