## 📌 Project Overview
This is a fully functional, automated Blackjack (21) game built in Python. It marks the first "Capstone" project of the course, requiring the integration of complex conditional logic, multiple while loops, and list manipulation.

## 🚀 Key Features
- **Dynamic Scoring:** Includes "Ace Logic" where the value of an Ace automatically shifts from 11 to 1 if the player's score exceeds 21.
- **Automated Dealer:** The computer player follows professional Blackjack rules, automatically drawing cards until it reaches a minimum score of 17.
- **Recursive Gameplay:** Allows users to restart the game immediately, clearing the console for a fresh experience.
- **Global Win/Loss Conditions:** Handles Blackjacks (score of 0), busts (over 21), and standard score comparisons.

## 🛠️ Technical Breakdown
1. **Helper Functions:** 
   - `deal_cards()`: Uses `random.choice` to simulate a deck.
   - `calculate_score()`: Processes the hand to check for Blackjacks and manage Ace values.
   - `compare()`: An exhaustive evaluation of the user vs. computer scores.
2. **State Management:** Initializing scores and game-over flags to manage the flow of the `while` loops.
3. **User Input Handling:** Manages the "Hit" or "Pass" decision-making process.

## 📖 Lessons Learned
- **Refactoring:** The importance of moving helper functions to the top for better readability.
- **Initialization:** Why variables must be defined before being called in a loop (avoiding `NameError`).
- **Complex Logic Flow:** Managing the transition between the user's turn and the dealer's automated turn.