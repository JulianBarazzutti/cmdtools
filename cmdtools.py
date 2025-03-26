# cmdtools.py

from user import User
from core import Core
from calculator import Calculator

class CmdTools:
    def __init__(self, user: User):
        self.user = user
        self.calculator = Calculator()

    def show_menu(self):
        print("\nChoose an option:")
        print("1. Greet me")
        print("2. Show current time")
        print("3. Show current date")
        print("4. Show inspirational quote")
        print("5. Calculator")
        print("6. Exit")

    def handle_choice(self, choice):
        if choice == "1":
            print(self.user.greet())
        elif choice == "2":
            print(f"The current time is: {Core.get_time()}")
        elif choice == "3":
            print(f"Today's date is: {Core.get_date()}")
        elif choice == "4":
            print(f"🌟 {Core.get_inspirational_quote()}")
        elif choice == "5":
            self.calculator.calculate()
        elif choice == "6":
            print("👋 Goodbye!")
            return False
        else:
            print("⚠️ Invalid choice. Please select a number from 1 to 6.")
        return True

    def run(self):
        print("🛠️ Welcome to cmdtools!")
        print(self.user.personalized_time_greeting())

        while True:
            self.show_menu()
            choice = input("Enter your choice (1-6): ").strip()
            if not self.handle_choice(choice):
                break
