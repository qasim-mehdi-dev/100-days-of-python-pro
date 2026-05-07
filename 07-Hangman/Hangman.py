import random
from Hangman_art import stages, logo
from Hangman_words import word_list



chosen_word = random.choice(word_list)
print(chosen_word)
print(logo)

lives = 6

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    print(f"****************{lives}/6 lives remaining**************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"Your guessed letter doesn't exist in the word. You lose a life!")
    if lives == 0:
        game_over = True
        print(f"The word you had to guess was {chosen_word}. You Lose!")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])