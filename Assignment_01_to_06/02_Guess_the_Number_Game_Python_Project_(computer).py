import random 

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    number_to_guess = random.randint(1, 100)
    attempts = 0 


    while True :

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

        

guess_the_number()