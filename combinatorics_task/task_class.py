"""
Problem:
There is a certain number of students in a class. On Tuesday, an
inspection is scheduled to visit the school. Therefore, a group of students
is required to serve as "extras." The identity of the students does not
matter. How many ways are there to select?
"""

# Solution
# Import math library
import math

# Create function, that takes the numbers of all students and chosen
# Students. Check if numbers are valid, and calculate the number of
# Combinations

def combination():
    while True:
        try:
            all_students = int(input("Enter the number of all students in the class: "))
            chosen_students = int(input("Enter the number of all chosen from the class: "))
        except ValueError:
            print("Enter the total number please")
            continue


        if not (1 <= all_students <= 50) or not (1 <= chosen_students <= 50):
            print("Please enter a valid number")
        elif chosen_students > all_students:
            print("You cannot choose more people than you have in the class")
        else:
            break

    result = math.comb(all_students, chosen_students)
    print(f"There are {result} possible combinations")

# Use function
combination()

