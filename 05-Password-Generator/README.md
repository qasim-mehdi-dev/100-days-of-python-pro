🔐 Password Generator
A Python project that generates a secure, randomized password based on user-defined character preferences.
---
📌 About
This project was built in two versions:
Easy Version – Generates a password by directly concatenating random characters into a string.
Hard Version – Improves on the easy version by storing characters in a list first, shuffling them for true randomness, then joining into a final password.
---
🚀 How It Works
The user specifies how many letters, symbols, and numbers they want in the password.
Random characters are picked from predefined character sets.
(Hard version only) The characters are shuffled so the password isn't predictable.
The final password is printed.
---
🧠 Key Concepts Used
`random.choice()` – Picks a random item from a list
`random.shuffle()` – Shuffles a list in place (used in hard version)
`list.append()` – Adds characters to a list before joining
f-strings – For displaying the final password
