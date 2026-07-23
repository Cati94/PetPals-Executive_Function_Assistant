"""
Banner do PetPals.
"""

from rich.console import Console

console = Console()


def show_banner() -> None:
    """Mostra o banner inicial."""

    console.print(
        """
╔════════════════════════════════════╗
║            🐾 PetPals              ║
║     Personal AI Executive Agent    ║
╚════════════════════════════════════╝
""",
        style="cyan",
    )