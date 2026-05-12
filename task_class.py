"""
Problem:
There is a certain number of students in a class. On Tuesday, an
inspection is scheduled at the school. Therefore, a group of students
is required to serve as "extras." The identity of the students does not
matter. How many combinations are possible to select students for the
event?
"""

# Solution
# Import math library
import math

# Create function, that take numbers of all students and choosen
# Check if numbers are real, and calculate variation of combination

def combination():
    while True:
        try:
            all_students = int(input("Write a number of all students in class: "))
            chosen_students = int(input("Write a number of all choosen from class: "))
        except ValueError:
            print("Write a number please")
            continue


        if not (1 <= all_students <= 50) or not (1 <= chosen_students <= 50):
            print("Write a correct number")
        elif chosen_students > all_students:
            print("You cannot choose more people than you have in class")
        else:
            break

    result = math.comb(all_students, chosen_students)
    print(f"There are {result} possible combinations")

# Use function
combination()

