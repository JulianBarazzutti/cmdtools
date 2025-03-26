import datetime
import random

class Core:
    @staticmethod
    def greet(name: str) -> str:
        return f"Nice to meet you, {name}!"  # Added greet method

    @staticmethod
    def get_time() -> str:
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    @staticmethod
    def get_date() -> str:
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")

    @staticmethod
    def get_inspirational_quote() -> str:
        quotes = [
            "Keep going. Everything you need will come to you at the perfect time.",
            "You are stronger than you think.",
            "Stay focused. Stay consistent. Stay strong.",
            "One step at a time is all it takes to get you there.",
            "Discipline is remembering what you want.",
            "The struggle you're in today is developing the strength you need for tomorrow.",
            "Progress, not perfection."
        ]
        return random.choice(quotes)
