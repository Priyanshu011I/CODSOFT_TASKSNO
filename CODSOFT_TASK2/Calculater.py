def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return the remainder."""
    if b == 0:
        return None
    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def floor_divide(a, b):
    """Return floor division result."""
    if b == 0:
        return None
    return a // b


def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def display_menu():
    """Display calculator menu."""
    print("\n" + "=" * 50)
    print("              PYTHON CALCULATOR")
    print("=" * 50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Exit")
    print("=" * 50)


def calculate(choice, num1, num2):
    """Perform calculation based on user's choice."""

    if choice == "1":
        return add(num1, num2)

    elif choice == "2":
        return subtract(num1, num2)

    elif choice == "3":
        return multiply(num1, num2)

    elif choice == "4":
        return divide(num1, num2)

    elif choice == "5":
        return modulus(num1, num2)

    elif choice == "6":
        return power(num1, num2)

    elif choice == "7":
        return floor_divide(num1, num2)

    return None


def main():
    """Run the calculator application."""

    print("\nWelcome to the Python Calculator!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("\nThank you for using the Python Calculator!")
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nInvalid choice! Please select a number from 1 to 8.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice in ["4", "5", "7"] and num2 == 0:
            print("\nError: Division by zero is not allowed.")
            continue

        result = calculate(choice, num1, num2)

        print("\n" + "-" * 50)
        print(f"Result: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()