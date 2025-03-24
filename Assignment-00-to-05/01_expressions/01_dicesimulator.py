import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1 : {die1}, Die 2 : {die2}")


for i in range(3):
    print(f"Roll {i + 1} :")
    roll_dice()
    print()