import random
import string
import os
from collections import Counter

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words():
    with open("words.txt", "r") as file:
        words_list = [line.strip() for line in file]

    return words_list

def get_random_word(words):
    return random.choice(words)

def colorize(text, color):
    colors = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'dim': '\033[2m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

def display_alphabet(used_letters, correct_letters, misplaced_letters):
    better_looking_alphabet = """q w e r t y u i o p
 a s d f g h j k l
   z x c v b n m"""
    result = ''
    for line in better_looking_alphabet.split('\n'):
        for letter in line:
            if letter in correct_letters:
                result += colorize(letter, 'green')
            elif letter in misplaced_letters:
                result += colorize(letter, 'yellow')
            elif letter in used_letters:
                result += colorize(letter, 'dim')
            else:
                result += letter
        result += '\n'
    print(result)

def main():
    clear()
    words = load_words()
    target_word = get_random_word(words)
    max_attempts = 6
    attempts = 0
    used_letters = set()
    correct_letters = set()
    misplaced_letters = set()
    guesses = []

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()
        clear()

        if len(guess) != len(target_word):
            print(f"Please enter a {len(target_word)}-letter word.\n")
            continue

        if guess not in words:
            print("Not in word list. Try again.\n")
            continue

        attempts += 1
        result = ''
        target_counter = Counter(target_word)
        guess_counter = Counter(guess)

        for i, letter in enumerate(guess):
            used_letters.add(letter)
            if letter == target_word[i]:
                result += colorize(letter, 'green')
                correct_letters.add(letter)
                target_counter[letter] -= 1
            elif letter in target_word and guess_counter[letter] <= target_counter[letter]:
                result += colorize(letter, 'yellow')
                misplaced_letters.add(letter)
                target_counter[letter] -= 1
            else:
                result += colorize(letter.lower(), 'dim')

        for i in range(len(guesses)):
            print(f"       {guesses[i]}")
        guesses.append(result)
        print(f"       {result}")
        times = max_attempts - attempts
        print("\n" * times)
        display_alphabet(used_letters, correct_letters, misplaced_letters)

        if guess == target_word:
            print(f"Congratulations! You guessed the word in {attempts} attempts.")
            return

    print(f"Sorry, you've run out of attempts. The word was {target_word}.")


if __name__ == "__main__":
    main()
