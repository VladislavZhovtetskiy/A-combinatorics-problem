# A Password Generator Task

A Python program that takes a string of symbols from the user, shuffles them randomly, and generates 5 unique password options stored in a dictionary.

## What It Does
1. **User Input:** Prompt the user to enter a sequence of characters or a specific word.
2. **Data Cleaning:** Automatically trims whitespace and converts the input to lowercase for consistency.
3. **Randomized Shuffling:** Uses Python's built-in `random` module to shuffle the provided symbols uniquely for each option.
4. **Automated Iteration:** Runs a `for` loop with a fixed range to generate exactly 5 different password variations.
5. **Structured Storage:** Saves each generated password into a dictionary where the key is the option number and the value is the password string.

## How to Run (Quick Start)
Make sure you are in the project root and your virtual environment is active, then run:
```bash
python password_generator/generator.py



