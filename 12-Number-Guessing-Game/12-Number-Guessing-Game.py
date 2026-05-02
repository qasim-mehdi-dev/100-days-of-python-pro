from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("You guessed too high.")
        return turns-1
    elif user_guess < actual_answer:
        print("You guessed too low.")
        return turns-1
    else:
        print(f"You got it. The answer was {actual_answer}.")
        return turns


def set_difficulty():
    level = input("Chose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You ran out of guesses. You lose the answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again!.")
game()
