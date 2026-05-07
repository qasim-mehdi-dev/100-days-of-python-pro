# Day 8: Caesar Cipher (Python)

## 📌 Project Overview
A command-line tool that performs Caesar Cipher encryption and decryption. This project demonstrates the implementation of a shift-cipher algorithm, focusing on modular arithmetic and function optimization in Python.

## 🚀 Key Features
- **Bidirectional Logic:** A single, unified `caesar()` function that handles both encoding and decoding by manipulating the shift direction.
- **Edge-Case Handling:** Uses the modulo operator (`%`) to allow for "infinite" wrap-around of the alphabet, ensuring the program never crashes regardless of the shift size.
- **Dynamic User Interface:** Interactive inputs for message content, shift amount, and operation type.

## 🛠️ Technical Breakdown
1. **Mathematical Shift:** Instead of using complex `if/else` ladders for the alphabet, the program calculates positions using `alphabet.index(letter) + shift_amount`.
2. **Modular Arithmetic:** The use of `index % 26` ensures that a shift of 1 from 'z' correctly returns to 'a'.
3. **Parameter Optimization:** Refactored from two separate functions (`encrypt` and `decrypt`) into one universal function to adhere to the DRY (Don't Repeat Yourself) principle.

## 📖 Lessons Learned
- **Scope & Loops:** Understanding why state changes (like multiplying the shift by -1) must happen *outside* the loop to prevent cascading logic errors.
- **Positional vs. Keyword Arguments:** Implementing clean function calls for better readability.
- **Input Sanitization:** Using `.lower()` to ensure consistency between user input and the alphabet list.