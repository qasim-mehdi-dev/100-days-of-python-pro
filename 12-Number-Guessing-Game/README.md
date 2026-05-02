# Day 12: The Number Guessing Game

## 📌 Project Overview
A terminal-based game that challenges users to guess a randomly generated number between 1 and 100. This project serves as a deep dive into **Namespace** and **Scope** within Python.

## 🚀 Key Features
- **Difficulty Scaling:** Implements two modes (Easy/Hard) that dictate the number of attempts available to the player.
- **State Feedback:** Real-time analysis of user guesses ("Too high" or "Too low") to guide the player toward the answer.
- **Persistent Logic:** Uses a while loop controlled by both the accuracy of the guess and the remaining "lives" of the player.

## 🛠️ Technical Breakdown
1. **Global Constants:** Utilized `EASY_LEVEL_TURNS` and `HARD_LEVEL_TURNS` as global constants to maintain "clean" code and avoid magic numbers.
2. **Functional Returns:** The project relies heavily on the `return` keyword to pass updated turn counts from helper functions back to the main game engine.
3. **Local Scope:** All game-sensitive variables (like the actual answer) are kept within the local scope of the `game()` function to prevent accidental modification.

## 📖 Lessons Learned
- **Scope vs. Functionality:** Understanding the difference between local and global scope and how it affects variable accessibility.
- **The Power of Return:** Seeing how `return` acts as the bridge between isolated functions.
- **UI/UX in CLI:** Implementing a clear user interface using ASCII art and consistent spacing.

---
