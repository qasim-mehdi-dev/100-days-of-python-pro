# Day 10: Recursive Calculator (Python)

## 📌 Project Overview
A professional-grade CLI calculator that supports continuous calculations and recursive resets. This project demonstrates advanced function usage, including functions as first-class objects and the implementation of recursion.

## 🚀 Key Features
- **Dictionary-Based Dispatch:** Replaces complex conditional logic by mapping mathematical operators directly to functions.
- **State Preservation:** Allows users to "accumulate" results, using the output of the previous calculation as the input for the next.
- **Recursive Reset:** Uses recursion to clear the state and restart the application without exiting the program.

## 🛠️ Technical Breakdown
1. **First-Class Functions:** Storing function names in a dictionary: `operations = {"+": add}`.
2. **Recursive Logic:** Calling `calculator()` within itself to handle the "New Calculation" flow.
3. **Float Precision:** Handling decimal inputs for higher mathematical accuracy.

## 📖 Lessons Learned
- **Functions with Outputs:** Mastering the `return` keyword to pass data between execution blocks.
- **Call Stack Management:** Understanding when to use a loop vs. when to use recursion.
- **DRY Principle:** Using a dictionary to avoid repeating `input()` and `if` statements.

---
*Part of the 100 Days of Code Challenge.*