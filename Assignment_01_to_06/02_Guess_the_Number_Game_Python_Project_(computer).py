print("Think of a number between 1 and 100, and I will try to guess it!")
input("Press Enter when you're ready...")

low = 1
high = 100
attempts = 0

while True:
    if low > high:
        print("Hmm... Are you sure you're giving the right hints?")
        break

    guess = (low + high) // 2
    attempts += 1
    print(f"Is it {guess}?")

    feedback = input("Type 'h' if my guess is too high, 'l' if it's too low, or 'c' if it's correct: ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print(f"Yay! I guessed your number in {attempts} attempts!")
        break
    else:
        print("Please enter only 'h', 'l', or 'c'.")
