import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors (or 'q' to quit): ").lower()
    if choice in ['rock', 'paper', 'scissors', 'q']:
        return choice
    else:
        print("Invalid choice. Try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("=== Rock, Paper, Scissors Game ===")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

# Run the game
play_game()
