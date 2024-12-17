
# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. 
# The gun beats the snake, the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else statements. 
# Do not create any fancy GUI. Use proper functions to check for win.
import random

def game():
    choices = ["snake","water","gun"]
    computer = random.choice(choices)
    
    user  = input('''Enter Chocies ("Snake","Water","Gun"): ''').lower()
    if user not in choices:
        print("Not Valid option")
    
    print("Computer choices:" + computer)

    if(user == computer):
        print("Its Tie")
    elif (user == "snake" and computer == "gun") or (user == "water" and computer == "snake") or (user == "gun" and computer == "water"):
        print("You lose")
    else:
        print("You win") 

game()