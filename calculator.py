# calculator.py

class Calculator:
    def __init__(self):
        self.history = []

    def get_valid_number(self, prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def get_valid_operation(self) -> str:
        valid_operations = [
            "add", "subtract", "multiply", "divide",
            "exponentiate", "modulo", "floor"
        ]
        while True:
            op = input("Choose operation (add, subtract, multiply, divide, exponentiate, modulo, floor): ").strip().lower()
            if op in valid_operations:
                return op
            print("⚠️ Invalid operation. Please choose a valid one.")

    def calculate(self):
        first_number = self.get_valid_number("Enter first number: ")
        second_number = self.get_valid_number("Enter second number: ")
        operation = self.get_valid_operation()

        operations = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b if b != 0 else float('inf'),
            "exponentiate": lambda a, b: a ** b,
            "modulo": lambda a, b: a % b,
            "floor": lambda a, b: a // b
        }

        try:
            result = operations[operation](first_number, second_number)
            print(f"Result: {result}")
            self.log_calculation(result)
            self.log_to_file(result)
        except ZeroDivisionError:
            print("⚠️ Cannot divide by zero.")

    def log_calculation(self, result):
        self.history.append(result)
        print("History of calculations:")
        for res in self.history:
            print(res)

    def log_to_file(self, result):
        with open("calculations.txt", "a") as file:
            file.write(f"Result: {result}\n")
        print("Logged result to calculations.txt.")
