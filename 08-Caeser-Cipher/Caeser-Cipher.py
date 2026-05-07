import art
print(art.logo)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
            if letter not in original_text:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]

    print(f"Here is your {encode_or_decode} message: {output_text}")

play_again = True
while play_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)

    choice = input("Type 'yes' if you want to play, otherwise type 'no':\n").lower()
    if choice == "no":
        play_again = False
        print("Goodbye!")