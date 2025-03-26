# user.py

import datetime

class User:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Nice to meet you, {self.name}!"

    def get_time_greeting(self) -> str:
        """Returns a greeting based on the current time."""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning!"
        elif 12 <= hour < 18:
            return "Good afternoon!"
        elif 18 <= hour < 22:
            return "Good evening!"
        else:
            return "Good night!"

    def personalized_time_greeting(self) -> str:
        return f"{self.get_time_greeting()} Nice to see you, {self.name}."
