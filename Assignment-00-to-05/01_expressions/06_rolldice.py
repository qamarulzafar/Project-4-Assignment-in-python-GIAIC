# Simulate rolling two dice, and prints results of each roll as well as the total.


import random 

def main():
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)


    total: int = die1 + die2

    print("Dies have", 6, "sides each.")
    print("First Die:", die1)
    print("Second Die:", die2)
    print("Total of Two dies:", total)

main()
