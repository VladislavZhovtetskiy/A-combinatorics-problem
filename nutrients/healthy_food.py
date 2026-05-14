'''
Technical task
The user enters his data (gender, weight, height, age, activity level),
The program should calculate the calorie rate per day. And then
Approximately the norm of proteins, carbohydrates, and fats is
Rrescribed. We use the Mifflin-San Geor formula
'''

# Solution
# Ask user data
def user_data():
    while True:
        try:
            weight = float(input("Please, enter your current weight (kg): "))
            if 30 <= weight <= 250:
                break
            print("Please enter a valid weight (30-250 kg)")
        except ValueError:
            print("Enter a correct numeric value please")

    while True:
        try:
            height = float(input("Please, enter your current height (cm): "))
            if 120 <= height <= 250:
                break
            print("Please enter a valid height (120-250 cm)")
        except ValueError:
            print("Enter a correct numeric value please")

    while True:
        try:
            age = int(input("Please, enter your current age: "))
            if 15 <= age <= 100:
                break
            print("Please enter a valid age (15-100 years)")
        except ValueError:
            print("Enter a correct numeric value please")

    while True:
        gender = input("Please, enter your gender (male/female): ").strip().lower()
        if gender == "male" or gender == "female":
            break
        print("Please enter whether you are male or female")

    while True:
        activity = input("Please, enter your activity level (sit/low/mid/high/extreme): ").strip().lower()
        if activity in ["sit", "low", "mid", "high", "extreme"]:
            break
        print("Please enter a correct value of your current activity level")

    return weight, height, age, gender, activity
# Create function, that calculate bmr due to data

def calculate_bmr(gender, height, age, weight):
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

# Calculates Basal Metabolic Rate using the Mifflin-San Jeor formula

def calculate_tdee(bmr, activity):
    activity_coefficients = {
        "sit": 1.2,
        "low": 1.375,
        "mid": 1.55,
        "high": 1.725,
        "extreme": 1.9
    }
    return round(bmr * activity_coefficients[activity])

# Calculates Total Daily Energy Expenditure (TDEE) based on activity level
def calculate_macros(calories):
    proteins = round((calories * 0.30) / 4)
    fats = round((calories * 0.30) / 9)
    carbohydrates = round((calories * 0.40) / 4)

    return proteins, fats, carbohydrates

# Main execution
weight, height, age, gender, activity = user_data()
bmr = calculate_bmr(gender, height, age, weight)
total_calories = calculate_tdee(bmr, activity)
proteins, fats, carbs = calculate_macros(total_calories)

#
print("\n" + "="*30)
print(f"Your daily calorie norm: {total_calories} kcal")
print("-"*30)
print(f"Proteins: {proteins} g")
print(f"Fats: {fats} g")
print(f"Carbohydrates: {carbs} g")
print("="*30)

