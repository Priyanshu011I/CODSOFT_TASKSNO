import random


CHOICES = ["rock", "paper", "scissors"]


def get_user_choice():
    """Get a valid choice from the user."""

    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            return "rock"

        elif choice == "2":
            return "paper"

        elif choice == "3":
            return "scissors"

        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")


def get_computer_choice():
    """Generate a random choice for the computer."""

    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round."""

    if user_choice == computer_choice:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[user_choice] == computer_choice:
        return "user"

    return "computer"


def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and computer."""

    print("\n" + "-" * 50)
    print(f"Your Choice     : {user_choice.capitalize()}")
    print(f"Computer Choice : {computer_choice.capitalize()}")
    print("-" * 50)


def display_result(result):
    """Display the result of the round."""

    if result == "user":
        print("🎉 You Win!")

    elif result == "computer":
        print("🤖 Computer Wins!")

    else:
        print("🤝 It's a Tie!")


def display_score(user_score, computer_score, ties):
    """Display current game score."""

    print("\n" + "=" * 50)
    print("CURRENT SCORE")
    print("=" * 50)
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {ties}")
    print("=" * 50)


def play_game():
    """Run the Rock-Paper-Scissors game."""

    user_score = 0
    computer_score = 0
    ties = 0

    print("\n" + "=" * 50)
    print("       ROCK - PAPER - SCISSORS GAME")
    print("=" * 50)

    while True:

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)

        display_result(result)

        if result == "user":
            user_score += 1

        elif result == "computer":
            computer_score += 1

        else:
            ties += 1

        display_score(user_score, computer_score, ties)

        play_again = input(
            "\nDo you want to play another round? (y/n): "
        ).strip().lower()

        if play_again != "y":
            break

    print("\n" + "=" * 50)
    print("             FINAL RESULT")
    print("=" * 50)

    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {ties}")

    if user_score > computer_score:
        print("\n🏆 Congratulations! You won the game!")

    elif computer_score > user_score:
        print("\n🤖 Computer won the game. Better luck next time!")

    else:
        print("\n🤝 The game ended in a tie!")

    print("=" * 50)
    print("Thank you for playing!")


def main():
    """Main program function."""

    play_game()


if __name__ == "__main__":
    main()