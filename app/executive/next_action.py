"""
PetPals - Next Action.

Representa a próxima melhor ação sugerida
ao utilizador pelo Executive Function Engine.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class NextAction:
    """Representa uma única ação recomendada."""

    title: str
    reason: str
    estimated_minutes: int
    cognitive_load: str
    confidence: float

    total_steps: int = 1
    current_step: int = 1
    requires_break: bool = False
    show_only_next_step: bool = True

    @property
    def progress(self) -> float:
        """Percentagem de progresso da tarefa."""

        if self.total_steps <= 0:
            return 0.0

        return (self.current_step / self.total_steps) * 100

    def __str__(self) -> str:
        """Apresentação amigável da próxima ação."""

        return (
            "\n"
            "🐾 Próxima ação\n"
            "-------------------------\n"
            f"Tarefa: {self.title}\n"
            f"Motivo: {self.reason}\n"
            f"Tempo: {self.estimated_minutes} min\n"
            f"Carga cognitiva: {self.cognitive_load}\n"
            f"Confiança: {self.confidence:.0%}\n"
            f"Passo: {self.current_step}/{self.total_steps}\n"
            f"Progresso: {self.progress:.0f}%"
        )
