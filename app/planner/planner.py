from app.user.user_state import Energy


class Planner:

    def suggest(self, state):

        print("\n🐾 Sugestão do PetPals\n")

        if state.energy == Energy.VERY_LOW:
            print("Hoje parece um dia difícil.")
            print("Vamos escolher tarefas muito simples.")

        elif state.energy == Energy.LOW:
            print("Sugiro tarefas curtas e com pouca carga cognitiva.")

        elif state.energy == Energy.NORMAL:
            print("Hoje podes alternar entre tarefas médias e pequenas.")

        elif state.energy == Energy.HIGH:
            print("Bom momento para avançar num projeto importante.")

        elif state.energy == Energy.VERY_HIGH:
            print("Excelente dia para atacar tarefas mais complexas!")
