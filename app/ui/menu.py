from app.services.task_service import TaskService


class Menu:
    """Menu principal do PetPals."""

    def __init__(self):
        self.task_service = TaskService()

    def show(self):
        while True:
            print("\n🐾 PetPals")
            print("----------------")
            print("1 - Criar tarefa")
            print("2 - Listar tarefas")
            print("3 - Sair")

            option = input("\nEscolha: ")

            if option == "1":
                self.create_task()

            elif option == "2":
                self.list_tasks()

            elif option == "3":
                print("Até breve! 🐾")
                break

            else:
                print("Opção inválida.")

    def create_task(self):
        title = input("Título: ")

        task = self.task_service.create_task(
            title=title
        )

        print(
            f"✅ Tarefa criada: {task.title}"
        )

    def list_tasks(self):
        tasks = self.task_service.list_tasks()

        if not tasks:
            print("Não existem tarefas.")

        else:
            print("\n📋 Tarefas:")

            for task in tasks:
                print(
                    f"{task.id} - {task.title} "
                    f"({task.status.value})"
                )
