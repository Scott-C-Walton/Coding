year = int(input("What year would you like to find out if it is a leap year? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("That is a leap year!")
    else:
      print("That is not a leap year.")
  else:
    print("That is a leap year!")
else:
  print("That is not a leap year.")
