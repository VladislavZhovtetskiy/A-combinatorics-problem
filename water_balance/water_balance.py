"""
Problem
My sister wants to know, how much water she needs to drink every day.
But it is difficult to calculate that every time. For that purpose i
Created a program, that asks the user to enter gender, age, height,
Weight and cup volume, and his or her activity. After that, the user
Sees how many cups of water they need to drink
"""

# Solution
# Create a function that accept user weight, gender, age and validates them

def get_user_parameters():
    while True:
        try:
            height = int(input("Enter your height in cm please: "))
            weight = int(input("Enter your weight in kg please: "))
            age = int(input("Enter your age please: "))
        except ValueError:
            print("Please enter a valid value")
            continue

        if height <= 150 or height >= 220:
            print("Please enter a valid value")
            continue
        elif weight <= 50 or weight >= 150:
            print("Please enter a valid value")
            continue
        elif age < 18 or age > 70:
            print("Please enter a valid value")
            continue
        break
    return height, weight, age

# Create a function that accept user gender, activity and validates them
def user_details():
    while True:
        gender = input("Enter your gender(male\\female): ").strip().lower()
        activity = input("Enter your activity level(low\\mid\\high): ").strip().lower()

        if gender not in ["male", "female"]:
            print("Please enter whether you are male or female")
            continue
        elif activity not in ["low", "mid", "high"]:
            print("Please enter a value of your curent activity level(low/mid/high)")
            continue
        break
    return gender, activity
# Create a function that accept user`s cup volume and validates them.

def cup_parameters():
    while True:
        try:
            cup_volume = int(input("Enter a volume of your cup in ml: "))
        except ValueError:
            print("Enter a valid value")
            continue

        if not (cup_volume >= 100 and cup_volume % 50 == 0 ):
            print("Please enter a valid value")
            continue
        break
    return cup_volume
# Main function that calculate necessary cups of water and show it
# To the user

def water_manager():
    height, weight, age = get_user_parameters()
    gender, activity = user_details()
    cup_volume = cup_parameters()

    activity_bonuses = {"low": 50, "mid": 100, "high": 200}
    bonus = activity_bonuses[activity]

    if gender == "male":
        volume = int(weight * 35 + height * 1 - age * 2 + 250 + bonus - 15)
    else:
        volume = int(weight * 31 + height * 1 - age * 2 + 350 - 15 + bonus)

    result = round(volume / cup_volume, 1)
    print(f"You need to drink about {result} cup of water in 1 day")

# Base construction
if __name__ == "__main__":
    while True:
        water_manager()

        repeat = input("\nDo you want to calculate again? (yes/no): ").strip().lower()

        if repeat != "yes":
            print("Good luck! Stay hydrated! ")
            break
