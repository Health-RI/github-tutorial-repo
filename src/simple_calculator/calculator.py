# SPDX-FileCopyrightText: 2024 Stichting Health-RI
#
# SPDX-License-Identifier: apache-2.0


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


def main():
    calculator = Calculator()
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice in ("1", "2", "3", "4"):
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            if choice == "1":
                result = calculator.add(a, b)
            elif choice == "2":
                result = calculator.subtract(a, b)
            elif choice == "3":
                result = calculator.multiply(a, b)
            elif choice == "4":
                result = calculator.divide(a, b)
            print(f"{a} {['+', '-', '*', '/'][int(choice)-1]} {b} = {result}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
