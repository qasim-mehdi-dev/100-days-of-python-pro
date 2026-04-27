# Day 7: Hangman Game (Python)

## 📌 Project Overview
A command-line version of the classic Hangman game. This project was built to master complex logic flow, including nested loops, list manipulation, and state management in Python.

## 🚀 Key Features
- **Dynamic Word Selection:** Utilizes the `random` module to pull words from an external library.
- **State Persistence:** Tracks correctly guessed letters and remaining lives to manage game flow.
- **ASCII Art UI:** Interactive visual feedback through the command line using multi-line string art.
- **UX Protection:** Prevents the user from losing lives on duplicate guesses.

## 🛠️ Logic Breakdown
1. **The Game Loop:** A `while` loop that runs until the user wins or runs out of lives.
2. **String Reconstruction:** Every turn, the display string is rebuilt by checking the `chosen_word` against a memory list of `correct_letters`.
3. **Index Matching:** Syncing the number of `lives` with a list of ASCII stages to update the visual "Gallows."

## 📖 Lessons Learned
- **DRY Principle:** Keeping words and art in separate modules to keep the main logic clean.
- **Boolean Flags:** Using `game_over` to control high-level program state.
- **Input Sanitization:** Using `.lower()` to ensure user input doesn't break the logic.

---
*Part of the 100 Days of Code Challenge.*