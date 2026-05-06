import random
import os

# List of potential words
WORDS = ["transmission", "throttle", "compression", "combustion", "horsepower", "displacement", "octane", "gasoline"]

# Symbol used to represent hidden letters
HIDDEN_SYMBOL = "_"

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 6 

def choose_word_random():
    return random.choice(WORDS)

def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

def get_guessed_word(secret_word, guessed_letters):
    masked = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    return masked

def get_available_letters(guessed_letters):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining = "".join([char for char in alphabet if char not in guessed_letters])
    return remaining

def hints_match(pattern, candidate):
    if len(pattern) != len(candidate):
        return False
    else:
        return all(pattern[i] == "_" or pattern[i] == candidate[i] for i in range(len(pattern)))

def show_possible_matches(pattern):
    results = []
    for word in WORDS:
       if hints_match(pattern, word) == True:
           results.append(word)
    return results

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def hangman(secret_word):
    guessed_letters = []
    mistakes = 0
    stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    """]
    while mistakes < MAX_ATTEMPTS:
        if is_word_guessed(secret_word, guessed_letters) == True:
            break
        clear_screen()
        print (stages[mistakes])
        print (get_guessed_word(secret_word, guessed_letters))
        print (get_available_letters(guessed_letters))
        guess = input("Please guess a letter: ")
        if guess in secret_word:
            guessed_letters.append(guess)
        elif guess == "?":
            print (show_possible_matches(get_guessed_word(secret_word, guessed_letters)))
        else:
            guessed_letters.append(guess)
            mistakes += 1

def main():
    # Entry point for the game
    secret_word = choose_word_random()
    hangman(secret_word)


if __name__ == "__main__":
    main()
