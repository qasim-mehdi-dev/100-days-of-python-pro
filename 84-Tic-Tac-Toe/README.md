# Command-Line Tic-Tac-Toe

A robust, terminal-based implementation of the classic Tic-Tac-Toe game built with pure Python. The project focuses on rigorous state management, synchronous win/draw checking loops, and air-tight user input validation.

## 🚀 Features
* **Dynamic Grid Render:** Displays a clean 3x3 layout updated in real-time using string interpolation hooks.
* **Rigorous Input Validation:** Sanitizes player entries to prevent crashing from empty strings, out-of-bounds integers, non-numeric strings, or duplicated placement attempts.
* **Automated State Tracking:** Evaluates 8 distinct multi-index winning combinations or tie states instantaneously after every valid turn.
* **Modular Logic:** Structured with isolated functions handling distinct jobs (`display_board`, `check_win`, `check_draw`) to maintain clean, scalable execution.

## 🛠️ Logic & Structure
The game engine executes via a continuous `while` loop that handles:
1. Turn-based terminal prompts tracking state variables (`current_player`).
2. Index conversion maps matching user digits `1-9` seamlessly to Python's `0-8` list structures.
3. Post-move evaluation loops checking game termination rules before switching active player tokens.

## 📁 Repository Structure
```text
.
├── main.py        # Core functional logic and game engine execution loops
└── README.md      # Project dashboard documentation