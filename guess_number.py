import random


# In this function you have to guess the number that the computer has selected.
def guess(x):
    random_number = random.randint(1, x)
    guess_user = 0
    while guess_user != random_number:
        try:
            guess_user = int(input(f"Guess a number between 0 an {x}:"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess_user == random_number:
            print("Yeah you guessed right!")
            guess_user = random_number
        elif guess_user > random_number:
            print("Sorry your number isn`t right. Your guessed number is too high!")
        elif guess_user < random_number:
            print("Sorry your number isn`t right. Your guessed number is too low!")


# In this function the computer guesses the number that you have selected.
def computer_guess():
    try:
        x = int(input(f"Please enter the range of numbers for the game:"))
    except ValueError:
        print("An exception occurred.")

    margin = 0
    feedback = ""

    while feedback != "c":
        guess_computer = random.randint(margin, x)
        print(f"Is the number {guess_computer}?")
        feedback = input("Please enter if the number is too high = h, too low = l or correct=c").lower()
        if feedback == "h":
            x = guess_computer - 1
        elif feedback == "l":
            margin = guess_computer + 1
        elif feedback == "c":
            print(f"Yeah you guessed it right!")
            feedback = "c"


computer_guess()
