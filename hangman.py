import random
import string
from english_words import english_words_set


# Checking the words in a set if there is a space or "-".
def get_valid_word():
    random_word = random.choices([*english_words_set], k=1)
    while '-' in random_word or ' ' in random_word:
        random_word = random.choices([*english_words_set], k=1)

    return random_word


def hangman():
    word = get_valid_word()
    word = ''.join(word).upper()  # converts the list word into a string for upper()
    print(word)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # list of letters in alphabet
    used_letters = set()  # list of used letters during game




