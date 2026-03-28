import random

# Predefined list of words
words = ["python", "apple", "tiger", "chair", "water"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Display initial blanks
display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

# Game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The correct word was:", word)