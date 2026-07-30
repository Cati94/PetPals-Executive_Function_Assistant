from app.executive.next_action import NextAction

action = NextAction(
    title="Abrir o Visual Studio Code",
    reason=("Hoje tens pouca energia. " "Vamos começar por uma tarefa simples."),
    estimated_minutes=2,
    cognitive_load="low",
    confidence=0.96,
    total_steps=5,
    current_step=1,
    requires_break=False,
)

print(action)
