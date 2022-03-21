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
    alphabet = set(string.ascii_uppercase) # list of letters in alphabet
    used_letters = set()  # list of used letters during game

    while len(word) > 0:
        # tell the user which letters he already used
        print(f"Your have guessed these letters:", ' '.join(used_letters))

        # print what the current word is:
        word_list = [user_letter if user_letter in used_letters else '-' for user_letter in word]
        print("Current letters in word :", ' '.join(word_list))

        user_letter = input("Please enter one letter!:").upper()
        if user_letter in alphabet - used_letters:  # Checking already used words
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("you already used this letter.Try again!")
        else:
            print("This char is not a or ONE letter. Try again!")


question = input("Do you wanna play a game? y = Yes or n = No").lower()
if question == "y":
    print("nice")
    hangman()
else:
    print("okay")


