# Hangman-Guess-Game
Design a text-based Hangman game. The program
selects a random word, and the player guesses one
letter at a time to uncover the word. You can set a
limit on the number of incorrect guesses allowed.

Strengths:
Clean Code: The structure is simple and easy to understand.
Separation of Concerns: Functions like choose_word and display_word keep things modular.
Basic Error Handling: Duplicate letter checks prevent unnecessary errors.
User Interaction: The game provides clear feedback on each guess.
Areas for Improvement:
Customization: Allowing users to input a custom word list could enhance replayability.
Performance: Instead of checking all(letter in guessed_letters for letter in word), you could use set(word) <= guessed_letters for better readability and efficiency.
User Experience: Adding a visual hangman drawing would improve the gameplay.
Input Validation: Handling edge cases like non-alphabetic input or multiple characters would improve robustness.
Code Structure: Moving max_attempts as a parameter in hangman() could make it more configurable.
