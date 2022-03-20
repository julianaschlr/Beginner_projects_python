import random
import string
from english_words import english_words_set


# Checking the words in a set if there is a space or "-".
def get_valid_word():
    random_word = random.choices([*english_words_set], k=1)
    while '-' in random_word or ' ' in random_word:
        random_word = random.choices([*english_words_set], k=1)

    return random_word


def hangman(user_letter):
    word = get_valid_word()
    word = ''.join(word).upper()  # converts the list word into a string for upper()
    print(word)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # list of letters in alphabet
    used_letters = set()  # list of used letters during game

    if user_letter in alphabet - used_letters: # Checking already used words
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    else:

i = True
user_input = ""
while i is not False:
    user_input = input("Please enter one letter:").upper()
    if user_input.isdigit():
        print("Please enter a letter!!!")
    elif len(user_input) > 1:
        print("Please enter ONE letter!")
    elif user_input.isalpha():
        print("Here we go!")
    else:
        print("Whatever try again!")

hangman(user_input)
