import random

words = ['python', 'hangman', 'programming', 'code', 'developer']


word = random.choice(words)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman Game!")
print("_ " * len(word))

while tries > 0:
    guess = input("🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}")

    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(display.strip())

    
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"💀 Game Over! The word was '{word}'")
