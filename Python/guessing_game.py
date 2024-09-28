import math as m
import random

def guessing_game():
    print("Welcome to guessing Game!")
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Guess again: "))

    print(f"Congratulations! You guessed the number {secret_number} correctly!")


guessing_game()
