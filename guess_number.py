import random

def hangman():
    # List of words
    words = ['python', 'hangman', 'developer', 'programming', 'algorithm', 'variable']
    
    # Randomly select a word
    word = random.choice(words)
    word_length = len(word)
    guessed_word = ['_'] * word_length
    guessed_letters = set()
    attempts_left = 6  # Number of incorrect guesses allowed
    
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", attempts_left, "incorrect attempts allowed.")
    print("Word:", " ".join(guessed_word))
    
    while attempts_left > 0:
        guess = input("\nEnter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong guess. The letter '{guess}' is not in the word.")
            print(f"You have {attempts_left} attempts left.")
        
        print("Word:", " ".join(guessed_word))
        
        # Check if the player has guessed the word
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nYou ran out of attempts. The word was:", word)
    
    print("Game Over!")

# Run the game
hangman()