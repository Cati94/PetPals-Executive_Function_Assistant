"""
Decompositor de tarefas do PetPals.

Transforma uma tarefa grande numa sequência de passos pequenos.
"""


class TaskDecomposer:
    """Divide tarefas em passos executáveis."""

    def decompose(self, task):
        """
        Decompõe uma tarefa em passos.

        Por enquanto utiliza regras simples.
        Mais tarde poderá ser integrado com IA.
        """

        title = task.title.lower()

        if "readme" in title:
            return [
                "Abrir o projeto no terminal",
                "Abrir o ficheiro README.md",
                "Rever a estrutura do projeto",
                "Atualizar o README",
                "Guardar as alterações",
            ]

        if "bugs" in title or "bug" in title:
            return [
                "Abrir o projeto",
                "Reproduzir o primeiro erro",
                "Identificar a causa do erro",
                "Corrigir o erro",
                "Executar os testes",
            ]

        if "estudar" in title:
            return [
                "Abrir o material de estudo",
                "Escolher um tópico",
                "Estudar durante alguns minutos",
                "Fazer um pequeno exercício",
                "Registar o que foi aprendido",
            ]

        if "petpals" in title:
            return [
                "Abrir o projeto PetPals",
                "Verificar o estado atual",
                "Escolher uma pequena melhoria",
                "Implementar a melhoria",
                "Executar os testes",
            ]

        # Regra genérica
        return [
            f"Preparar: {task.title}",
            "Começar a tarefa",
            "Continuar o trabalho",
            "Rever o resultado",
            "Concluir a tarefa",
        ]
