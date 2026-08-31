"""Program 8: Number guessing game. The computer picks a random number in
a fixed range, the user guesses, and gets too high / too low / correct
feedback. Limited number of attempts."""

import random

LOW = 1
HIGH = 100
MAX_ATTEMPTS = 7


def get_valid_guess(prompt, low, high):
    """Keep asking until the user enters an integer within [low, high]."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if value < low or value > high:
            print(f"Please enter a number between {low} and {high}.")
            continue
        return value


def play_game(low=LOW, high=HIGH, max_attempts=MAX_ATTEMPTS):
    target = random.randint(low, high)
    attempts = 0

    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        guess = get_valid_guess(f"Attempt {attempts + 1}/{max_attempts} - your guess: ", low, high)
        attempts += 1

        if guess == target:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return

        if guess < target:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of attempts! The number was {target}.")


def main():
    play_game()


if __name__ == "__main__":
    main()
