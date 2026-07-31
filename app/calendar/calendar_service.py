from app.calendar.calendar_repository import CalendarRepository


class CalendarService:

    def __init__(self):

        self.repository = CalendarRepository()

    def today(self):

        return self.repository.today()
