from app.database.models import EnergyLevel, Priority
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
        print("\n🐾 Nova tarefa")

        title = input("Título: ")
        description = input("Descrição: ")

        print("\nPrioridade")
        print("1 - Baixa")
        print("2 - Média")
        print("3 - Alta")

        priority_option = input("Escolha: ")

        priority_map = {
            "1": Priority.LOW,
            "2": Priority.MEDIUM,
            "3": Priority.HIGH,
        }

        priority = priority_map.get(
            priority_option,
            Priority.MEDIUM,
        )

        print("\nEnergia necessária")
        print("1 - Baixa")
        print("2 - Média")
        print("3 - Alta")

        energy_option = input("Escolha: ")

        energy_map = {
            "1": EnergyLevel.LOW,
            "2": EnergyLevel.MEDIUM,
            "3": EnergyLevel.HIGH,
        }

        energy = energy_map.get(
            energy_option,
            EnergyLevel.MEDIUM,
        )

        estimated_minutes = int(input("\nTempo estimado (min): "))

        context = input("Contexto (computador, casa, rua...): ")

        task = self.task_service.create_task(
            title=title,
            description=description,
            priority=priority,
            energy_level=energy,
            estimated_minutes=estimated_minutes,
            context=context,
        )

        print(f"\n✅ Tarefa criada: {task.title}")

    def list_tasks(self):
        tasks = self.task_service.list_tasks()

        if not tasks:
            print("Não existem tarefas.")
            return

        print("\n📋 Tarefas:")

        for task in tasks:
            print(f"{task.id} - {task.title} " f"({task.status.value})")
