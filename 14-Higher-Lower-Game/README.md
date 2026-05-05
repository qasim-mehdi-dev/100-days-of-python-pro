# Day 14: Higher Lower Game

## 📌 Project Overview
The Higher Lower Game is the "Final Boss" of the Beginner Python module. It challenges the player to compare the follower counts of two social media accounts. This project integrates all core concepts learned in the first 14 days, including list manipulation, dictionary nesting, and complex game-state management.

## 🚀 Key Features
- **Data Driven:** Utilizes a custom dataset of 50 social media accounts.
- **Endless Gameplay:** As long as the player is correct, the winner of the previous round becomes the base for the next comparison.
- **Dynamic UI:** Includes custom ASCII art and a screen-clearing mechanism to provide a smooth user experience.
- **Input Normalization:** Handles various user input styles (uppercase/lowercase) and strips whitespace to prevent game-breaking errors.

## 🛠️ Technical Breakdown
1. **The Swap Logic:** Implemented a system where `Account A` is replaced by `Account B` after a successful round, ensuring the game flows continuously.
2. **First-Class Functions:** 
   - `format_data()`: Modularized the string formatting to keep the main game loop readable.
   - `check_answer()`: Separated the logical comparison from the UI feedback.
3. **Control Flow:** Managed an infinite `while` loop that terminates only when a specific boolean flag (`is_correct`) returns False.

## 📖 Lessons Learned
- **Architecture over Syntax:** Using the "Notebook Method" (Pseudocode) to plan the logic before writing code proved essential for managing this complex game flow.
- **Dictionary Management:** Improved efficiency in accessing nested data within lists.
- **Refactoring:** Learning to pull repetitive code out into separate functions to keep the project clean and maintainable.

---
