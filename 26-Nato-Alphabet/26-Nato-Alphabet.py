import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetics_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)

generate_phonetic()