print("WELCOME TO THE BMI CALCULATOR 2.0!")
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))
bmi = weight / (height * height)

if bmi < 18.5:
  print("You are under weight.")
elif bmi < 25: 
  print("You have a normal weight") 
elif bmi < 30:
  print("You are slightly overweight")
elif bmi < 35:
  print("You are obese")
else:
   print("You are clinicly obese")

