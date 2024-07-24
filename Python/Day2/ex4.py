print("Welcome to the tip calulator!!")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage would you like to tip? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = round(total_bill / people, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: $ {final_amount}")
