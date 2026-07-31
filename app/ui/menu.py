from app.database.models import EnergyLevel, Priority
from app.services.project_service import ProjectService
from app.services.task_service import TaskService


class Menu:
    """Menu principal do PetPals."""

    def __init__(self):
        self.task_service = TaskService()
        self.project_service = ProjectService()

    def show(self):

        while True:

            print("\n🐾 PetPals")
            print("----------------")
            print("1 - Criar tarefa")
            print("2 - Listar tarefas")
            print("3 - Criar projeto")
            print("4 - Listar projetos")
            print("5 - Sair")

            option = input("\nEscolha: ")

            if option == "1":
                self.create_task()

            elif option == "2":
                self.list_tasks()

            elif option == "3":
                self.create_project()

            elif option == "4":
                self.list_projects()

            elif option == "5":
                print("Até breve! 🐾")
                break

            else:
                print("Opção inválida.")

    def create_task(self):

        print("\n🐾 Nova tarefa")

        title = input("Título: ")
        description = input("Descrição: ")

        # ----------------------------
        # Escolha do projeto
        # ----------------------------

        projects = self.project_service.list_projects()

        project = None

        if projects:

            print("\n📂 Projeto")

            for p in projects:
                print(f"{p.id} - {p.name}")

            project_id = input("\nEscolha o projeto: ")

            project = next(
                (p for p in projects if str(p.id) == project_id),
                None,
            )

        # ----------------------------
        # Prioridade
        # ----------------------------

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

        # ----------------------------
        # Energia
        # ----------------------------

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
            project=project,
        )

        print(f"\n✅ Tarefa criada: {task.title}")

    def list_tasks(self):

        tasks = self.task_service.list_tasks()

        if not tasks:
            print("\nNão existem tarefas.")
            return

        print("\n📋 Tarefas")
        print("----------------")

        for task in tasks:

            project_name = task.project.name if task.project else "Sem projeto"

            print(
                f"{task.id} - {task.title} "
                f"[{project_name}] "
                f"({task.status.value})"
            )

    def create_project(self):

        print("\n📂 Novo Projeto")

        name = input("Nome: ")
        description = input("Descrição: ")

        project = self.project_service.create_project(
            name=name,
            description=description,
        )

        print(f"\n✅ Projeto '{project.name}' criado com sucesso!")

    def list_projects(self):

        projects = self.project_service.list_projects()

        if not projects:
            print("\nNão existem projetos.")
            return

        print("\n📂 Projetos")
        print("----------------")

        for project in projects:
            print(f"{project.id} - {project.name}")
