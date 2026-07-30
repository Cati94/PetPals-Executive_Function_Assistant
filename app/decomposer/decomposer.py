class TaskDecomposer:
    """
    Divide tarefas grandes
    em pequenos passos.
    """

    def decompose(self, title: str):

        rules = {
            "Preparar aula": [
                "Abrir a pasta da disciplina",
                "Escolher o tema",
                "Recolher materiais",
                "Criar os slides",
                "Rever a aula",
            ],
            "Programar PetPals": [
                "Abrir o VS Code",
                "Abrir o projeto",
                "Escolher a sprint",
                "Programar",
                "Fazer commit",
            ],
        }

        return rules.get(
            title,
            [
                "Analisar a tarefa",
                "Dividir em pequenas ações",
            ],
        )
