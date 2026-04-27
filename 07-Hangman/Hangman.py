import random
from Hangman_art import logo
from Hangman_art import stages
from Hangman_words import word_list

print(logo)

lives = 6
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"{lives}/6 Lives left!")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f" You have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess : " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f" You guessed {guess}. That's not in the word. You lose a life!")
        if lives == 0:
            game_over = True
            print(f"The correct word was {chosen_word}")
    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[lives])