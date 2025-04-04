# 🧩 Milestone #1: Generate Random Numbers


# import random 

# my_number = random.randint(1, 100)
# computer_number = random.randint(1, 100)

# print("Your number is: ", my_number)
# print("Computer number is: ", computer_number)


# # 🧩 Milestone #2: Get User Input


# guess = input("Do you think your number is higher or lower than the computer's?: ").lower()



# # 🧩 Milestone #3: Write Game Logic


# if guess == "higher" and my_number > computer_number:
#     print("You were right!")
# elif guess == "lower" and my_number < computer_number:
#     print("You were right!")
# else:
#     print("Aww, that's incorrect.")

# print("The computer's number was", computer_number)



# # 🧩 Milestone #4: Play Multiple Rounds


# NUM_ROUNDS = 5
# score = 0


# print("Welcome to the High-Low Game!")
# print("--------------------------------")


# for round_number in range(1, NUM_ROUNDS + 1):
#     print(f"Round {round_number}")

#     guess = input("Do you think your number is higher or lower than the computer's?: ").lower()


#     while guess not in ["higher", "lower"]:  # input validation
#         guess = input("Please enter either 'higher' or 'lower': ").lower()


#     if (guess == "higher" and my_number > computer_number) or (guess == "lower" and my_number < computer_number):
#         print("You were right!")
#         score += 1
#     else:
#         print("Aww, that's incorrect.")



#     print("The computer's number was", computer_number)
#     print("Your score is now", score)
#     print()  # blank line for spacing




# # 🧩 Milestone #5: Ending Message



# print("Thanks for playing!")

# if score == NUM_ROUNDS:
#     print("Wow! You played perfectly!")
# elif score >= NUM_ROUNDS // 2:
#     print("Good job, you played really well!")
# else:
#     print("Better luck next time!")






import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_number in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_number}")
    
    my_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print("Your number is", my_number)
    
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either 'higher' or 'lower': ").lower()

    if (guess == "higher" and my_number > computer_number) or (guess == "lower" and my_number < computer_number):
        print("You were right!")
        score += 1
    else:
        print("Aww, that's incorrect.")

    print("The computer's number was", computer_number)
    print("Your score is now", score)
    print()  # Blank line between rounds


print("Thanks for playing!")
if score == NUM_ROUNDS:
    print("🎉 Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("👍 Good job, you played really well!")
else:
    print("🙁 Better luck next time!")
