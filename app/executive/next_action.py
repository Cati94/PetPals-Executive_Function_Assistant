"""
PetPals
Next Action

Representa a próxima melhor ação sugerida
ao utilizador pelo Executive Function Engine.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class NextAction:
    """
    Representa uma única ação recomendada.

    Esta classe é o resultado final do
    Executive Function Engine.
    """

    # Nome da ação
    title: str

    # Explicação para o utilizador
    reason: str

    # Tempo estimado em minutos
    estimated_minutes: int

    # Carga cognitiva
    cognitive_load: str

    # Confiança da recomendação (0.0 a 1.0)
    confidence: float

    # Número de passos da tarefa
    total_steps: int = 1

    # Passo atual
    current_step: int = 1

    # Necessita pausa depois?
    requires_break: bool = False

    # Mostrar apenas este passo?
    show_only_next_step: bool = True

    @property
    def progress(self) -> float:
        """
        Percentagem de progresso da tarefa.
        """

        return (self.current_step / self.total_steps) * 100

    def __str__(self) -> str:
        return (
            f"\n"
            f"🐾 Próxima ação\n"
            f"-------------------------\n"
            f"Tarefa: {self.title}\n"
            f"Motivo: {self.reason}\n"
            f"Tempo: {self.estimated_minutes} min\n"
            f"Carga cognitiva: {self.cognitive_load}\n"
            f"Confiança: {self.confidence:.0%}\n"
            f"Passo: {self.current_step}/{self.total_steps}\n"
            f"Progresso: {self.progress:.0f}%"
        )
