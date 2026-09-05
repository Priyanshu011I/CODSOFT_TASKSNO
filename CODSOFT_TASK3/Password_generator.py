import secrets
import string


def get_password_length():
    """Get a valid password length from the user."""

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length must be at least 4 characters.")
                continue

            if length > 128:
                print("Password length cannot exceed 128 characters.")
                continue

            return length

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def generate_password(length):
    """Generate a secure random password."""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Make sure the password contains different character types
    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + numbers + symbols

    # Generate remaining characters
    for _ in range(length - 4):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 55)
    print("              PASSWORD GENERATOR")
    print("=" * 55)
    print("1. Generate Password")
    print("2. Exit")
    print("=" * 55)


def main():
    """Run the Password Generator application."""

    print("\nWelcome to the Password Generator!")

    while True:

        display_menu()

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":

            length = get_password_length()

            password = generate_password(length)

            print("\n" + "-" * 55)
            print("Generated Password:")
            print(password)
            print("-" * 55)

        elif choice == "2":

            print("\nThank you for using the Password Generator!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()