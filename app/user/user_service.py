from app.user.user_state import (
    UserState,
    Energy,
    Mood,
    Focus,
)


class UserService:

    def __init__(self):
        self.state = UserState()

    def ask_daily_status(self):

        print("\n🐾 Antes de começarmos...")

        print("\nComo está a tua energia?")

        print("1 Muito baixa")
        print("2 Baixa")
        print("3 Normal")
        print("4 Boa")
        print("5 Excelente")

        option = input("> ")

        energy_map = {
            "1": Energy.VERY_LOW,
            "2": Energy.LOW,
            "3": Energy.NORMAL,
            "4": Energy.HIGH,
            "5": Energy.VERY_HIGH,
        }

        self.state.energy = energy_map.get(
            option,
            Energy.NORMAL,
        )

        return self.state
