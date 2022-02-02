print("Welcome to Treasure Island.\nYour mission is to find the treasure")
c1 = input("You arrive at a crossroad. Where do you want to go? (Type 'left' or 'right') ").lower()
if (c1 == "right"):
    print("You fell into a hole. Game Over.")
elif(c1 == "left"):
    c2 = input("You come across a lake. There is an island in the middle of the lake. (Type 'wait' to wait for a boat. Type 'swim' to swim across.) ").lower()
    if (c2 == "swim"):
        print("You get attacked by an angry trout. Game Over.")
    elif (c2 == "wait"):
        c3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if (c3 == "red"):
            print("It's a room full of fire. Game Over.")
        elif (c3 == "yellow"):
            print("You found the treasure! You Win!")
        elif(c3 == "blue"):
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You starved to death. Game Over.")
else:
    print("You entered an unexceptable instruction. Game Over.")
    
