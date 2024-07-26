print("Thank you for choosing Python Pizza Delivery!")
size = input("What size pizza do you want? s / m / l ")
add_pepperoni = input("Do you want pepperoni? y / n ")
extra_cheese = input("Do you want extra cheese? y / n ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

'''
add pepperoni to small pizza = y +2
add pepperoni to medium pizza = y +3
add pepperoni to large pizza = y + 3
add extra cheese to any size = y + 1
'''
bill = 0
if size == "s":
  bill += small_pizza
elif size == "m":
  bill += medium_pizza
else:
  bill += large_pizza
if add_pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill += 3
if extra_cheese == "y":
  bill += 1
print(f"Your final bill is ${bill}.")
