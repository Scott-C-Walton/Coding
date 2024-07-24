print("Welcome to the Band Name Generator")

city = input("What is the name of the city your grew up in?\n ")

pet_name = input("What is your pet's name?\n ")

#string concat - BAD WAY!!
print("Your band name could be " + city + " " + pet_name)
#fstring.  WAY more popular and is the standard
print(f"Your band name could be {city} {pet_name}")