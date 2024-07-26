'''
water_level = 50
if water_level > 80:
  print("Drain water")
else:
  print("continue")
'''

'''
print("WELCOME TO THE ROLLERCOASTER!!!!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry shorty, you shall not pass")
'''

'''
number = int(input("Enter a number and I will tell you if it is odd or even. "))
print(number)

if number % 2 == 0:
  print("That is an even number!")
else:
  print("That is indeed an odd number!")
'''

'''
print("WELCOME TO THE ROLLERCOASTER!!!!")
height = int(input("What is your height in cm? "))


if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("How old are you? "))
  if age < 12:
      print("Please pay $5")
  elif age <= 18:
      print("Please pay $7")
  else:
      print("Please pay $12")
else:
  print("Sorry shorty, you shall not pass")
'''


print("WELCOME TO THE ROLLERCOASTER!!!!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("How old are you? "))
  if age < 12:
      bill = 5
      print("Child tickets are $5")
  elif age <= 18:
      bill = 7
      print("Youth tickets are $7")
  else:
      bill = 12
      print("Adult tickets are $12")
  wants_photo = input("Do you want a photo taken y or n? ")
  if wants_photo == "y":
    bill += 3
  print(f"Your final bill is ${bill}.")
else:
  print("Sorry shorty, you shall not pass")
