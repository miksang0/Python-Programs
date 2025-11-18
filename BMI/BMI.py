weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meter: "))
bmi = weight / (height ** 2)
print (f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You're underweight.")
elif 18.5 <= bmi < 25:
    print("You have normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
