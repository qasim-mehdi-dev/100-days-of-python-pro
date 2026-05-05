from art import logo, vs
from game_data import data
import random

def format_data(account):
    account_name = account['account_name']
    account_desc = account['account_desc']
    account_country = account['account_country']

    return (f"{account_name} a {account_desc} from {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    guess = input("Who has more followers? Type 'a' or 'b': ").strip().lower()

    print("\n" * 40)
    print(logo)

    followers_a = account_a['followers']
    followers_b = account_b['followers']

    is_correct = check_answer(guess, followers_a, followers_b)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


