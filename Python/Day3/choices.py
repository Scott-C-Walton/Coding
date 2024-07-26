print("Welcome to the game of choices. If you win, you will be rich! If you lose, you will die.")
direction = input("You are at a fork in the road. Will you go 'left' or 'right'")
if direction == "left":
  water = input("You have come to a dock. Will you wait for a boat or swim across? 'wait' or 'swim' ")
  if water == "wait":
    print("Your boat arrives and takes you to the other side of the lake safely")
    box = input("You come to three boxes, numbered 1 - 3.  Which number do you choose? ")
    if box == "1":
      print("You have chosen the box with the bars of gold! You are rich!")
    elif box == "2":
      print("You have opened a box of deadly spiders. You have died. So tragic.")
    else:
      print("You have opened a box that contained a bomb. WHEW! What a mess. So tragic.")
  else:
    print("You are eaten by alligators and die. So tragic.")
else:
  print("You wander in the fog until you are eaten by skinwalkers. So tragic")

