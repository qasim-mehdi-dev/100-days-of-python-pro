import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', ';': '-.-.-.', ':': '---...', 
    "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '!': '-.-.--', '&': '.-...', '@': '.--.-.'
}

def text_to_morse(text: str) -> str:
    morse_words = []

    words = text.upper().split()
   
    for word in words:
        morse_letters = []
        for char in word:
            if char in MORSE_CODE_DICT:
                morse_letters.append(MORSE_CODE_DICT[char])
            else:
                morse_letters.append('?')
    
    return ' / '.join(morse_words)

def main():
    print("=" * 50)
    print("          TEXT TO MORSE CODE CONVERTER       ")
    print("=" * 50)
    print("Type your message to convert, or type 'EXIT' to quit\n")

    while True:
        user_input = input("Enter text: ").strip()
        
        if not user_input:
            continue

        if user_input.upper() == "EXIT":
            print("\nExisting Converter. Clear skies and happy coding!")
            sys.exit()

        translated_output = text_to_morse(user_input)
        
        print(f"Morse code: {translated_output}")
        print("-" * 50)

if __name__ == "__main__":
    main()