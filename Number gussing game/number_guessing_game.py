import random

def play_game():
    """Play one round of the guessing game."""
    secret = random.randint(1, 100)
    attempts = 0

    print("I am thinking of a number between 1 and 100.")
    while True:
        guess_text = input("Your guess: ")
        if not guess_text.strip():
            print("Please enter a number.")
            continue

        try:
            guess = int(guess_text)
        except ValueError:
            print("That is not a valid number. Try again.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print(f"Well done! You guessed the number in {attempts} attempts.")
            break


def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
