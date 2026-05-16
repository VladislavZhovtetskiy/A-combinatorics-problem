'''
Task
Create a programm that takes symbols and make 5 random password and
Replace it to dictionary

'''

# Solution
# Import random
import random

# Ask user for symbols

user_symbols = input(" Please write a symbols to generate a password: ").strip().lower()

# Create an empty dict to save 5 passwords

passwords_dict = {}


# Mix symbols and contain it to variable ang go through 5 options
# Through the for loop

for i in range(5):
    mixed_passwords = random.sample(user_symbols, len(user_symbols))
    single_password = "".join(mixed_passwords)

    passwords_dict[f"Option {i + 1}"] = single_password

# Print result
print(passwords_dict)




