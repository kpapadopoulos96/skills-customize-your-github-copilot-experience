
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python. You will practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the initial game setup by defining a list of words and randomly selecting one for the player to guess. Display the hidden word as underscores and set the number of allowed incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of at least 5 words
- Display the word as underscores (e.g., `_ _ _ _ _`) at the start
- Set a maximum number of incorrect guesses (e.g., 6)

### 🛠️	Implement the Guessing Loop

#### Description
Create a loop that repeatedly prompts the player to guess a letter. Update the displayed word with correctly guessed letters and track incorrect guesses.

#### Requirements
Completed program should:

- Accept single-letter guesses from user input
- Reveal all matching positions when a correct letter is guessed
- Track and display the number of incorrect guesses remaining
- Prevent the player from guessing the same letter twice

### 🛠️	Handle Win and Lose Conditions

#### Description
End the game when the player has either guessed all letters in the word or run out of attempts. Display an appropriate message for each outcome.

#### Requirements
Completed program should:

- End the game with a win message when all letters are guessed
- End the game with a lose message when attempts are exhausted
- Reveal the full word on a loss
