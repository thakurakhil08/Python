# Snake Water Gun

# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.


# SOLUTION


import random

def checkwin(user, computer):

    if user == computer:
        return "Draw"

    elif user == 1 and computer == 0:
        return "You Win"

    elif user == 0 and computer == 1:
        return "Computer Wins"

    elif user == 0 and computer == 2:
        return "You Win"

    elif user == 2 and computer == 1:
        return "You Win"

    else:
        return "Computer Wins"


user = int(input("Enter 1 for Snake, 0 for Water, 2 for Gun: "))

computer = random.choice([0, 1, 2])


result = checkwin(user, computer)

print("You chose:", user)
print("Computer chose:", computer)
print(result)