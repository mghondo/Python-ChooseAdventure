# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Calculate BMI
bmi = weight / (height ** 2)

# Interpret BMI
if bmi < 18.5:
    interpretation = "you are underweight"
elif bmi < 25:
    interpretation = "you have a normal weight"
elif bmi < 30:
    interpretation = "you are slightly overweight"
elif bmi < 35:
    interpretation = "you are obese"
else:
    interpretation = "you are clinically obese"

# Print the result
print(f"Your BMI is {bmi}, {interpretation}.")
