from app.database.models import EnergyLevel, Priority
from app.services.project_service import ProjectService
from app.services.task_service import TaskService


class Menu:
    """Menu principal do PetPals."""

    def __init__(self):
        self.task_service = TaskService()
        self.project_service = ProjectService()

    def show(self):
        """Mostra o menu principal."""

        while True:
            print("\n🐾 PetPals")
            print("----------------")
            print("1 - Criar tarefa")
            print("2 - Listar tarefas")
            print("3 - Concluir tarefa")
            print("4 - Criar projeto")
            print("5 - Listar projetos")
            print("6 - Sair")

            option = input("\nEscolha: ")

            if option == "1":
                self.create_task()

            elif option == "2":
                self.list_tasks()

            elif option == "3":
                self.complete_task()

            elif option == "4":
                self.create_project()

            elif option == "5":
                self.list_projects()

            elif option == "6":
                print("Até breve! 🐾")
                break

            else:
                print("Opção inválida.")

    def create_task(self):
        """Cria uma nova tarefa."""

        print("\n🐾 Nova tarefa")

        title = input("Título: ")
        description = input("Descrição: ")

        projects = self.project_service.list_projects()
        project = None

        if projects:
            print("\n📂 Projeto")

            for project_item in projects:
                print(f"{project_item.id} - " f"{project_item.name}")

            project_id = input("\nEscolha o projeto " "(Enter = sem projeto): ")

            if project_id:
                project = next(
                    (
                        project_item
                        for project_item in projects
                        if str(project_item.id) == project_id
                    ),
                    None,
                )

                if project is None:
                    print("\n⚠️ Projeto não encontrado. " "A tarefa ficará sem projeto.")

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

        try:
            estimated_minutes = int(input("\nTempo estimado (min): "))
        except ValueError:
            estimated_minutes = 30
            print("⚠️ Valor inválido. " "A usar 30 minutos.")

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

        if project:
            print(f"📂 Projeto: {project.name}")
        else:
            print("📂 Projeto: Sem projeto")

    def list_tasks(self):
        """Lista todas as tarefas."""

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

    def complete_task(self):
        """Marca uma tarefa como concluída."""

        tasks = self.task_service.list_tasks()

        pending_tasks = [task for task in tasks if task.status.value != "done"]

        if not pending_tasks:
            print("\n🎉 Não existem tarefas pendentes.")
            return

        print("\n✅ Tarefas pendentes")
        print("----------------")

        for task in pending_tasks:
            project_name = task.project.name if task.project else "Sem projeto"

            print(f"{task.id} - {task.title} " f"[{project_name}]")

        try:
            task_id = int(input("\nID da tarefa a concluir: "))
        except ValueError:
            print("\n❌ ID inválido.")
            return

        task = self.task_service.complete_task(task_id)

        if task is None:
            print("\n❌ Tarefa não encontrada.")
            return

        print(f"\n✅ Tarefa '{task.title}' " "marcada como concluída!")

    def create_project(self):
        """Cria um novo projeto."""

        print("\n📂 Novo Projeto")

        name = input("Nome: ")
        description = input("Descrição: ")

        project = self.project_service.create_project(
            name=name,
            description=description,
        )

        print(f"\n✅ Projeto '{project.name}' " "criado com sucesso!")

    def list_projects(self):
        """Lista todos os projetos."""

        projects = self.project_service.list_projects()

        if not projects:
            print("\nNão existem projetos.")
            return

        print("\n📂 Projetos")
        print("----------------")

        for project in projects:
            print(f"{project.id} - {project.name}")
