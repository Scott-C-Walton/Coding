# Still a placeholder

height = input("How tall are you in meters? ")
weight = input("How much do you weigh in kg? ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = int(weight_as_int / height_as_float ** 2)

print(f"Your BMI is {bmi}.")
