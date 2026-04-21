# Day 4: Rock Paper Scissors - Logic & Randomization 👊✋✌️

## Project Overview
A classic Rock, Paper, Scissors game built to master the integration of Python Lists and the `random` module. This version was built from scratch following a 24-hour learning-retention cycle to solidify understanding of 0-based indexing and conditional win/loss logic.

## Key Learning Objectives
* **Data Structures:** Utilizing Lists to store game options and ASCII art.
* **Randomization:** Implementing `random.randint()` to generate computer moves.
* **Input Normalization:** Handling user choices and preventing "Index Out of Range" errors.
* **Nested Logic:** Managing the three-way relationship where Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.

## How to Play
1.  Run the script in your terminal.
2.  Type `0` for Rock, `1` for Paper, or `2` for Scissors.
3.  The computer will randomly generate its choice.
4.  The winner is determined based on the classic rules of the game.

## Challenges Overcome
* **The Circular Logic Trap:** Managing the specific edge case where the lowest index (0) beats the highest index (2).
* **Input Validation:** Ensuring the program doesn't crash if the user enters a number outside the 0-2 range.

cd---
