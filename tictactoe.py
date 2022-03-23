import random

game_template = [" ",
                 "1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function creates the template for the game
def show_game_template():
    print("-------------")
    print("|", game_template[1], "|", game_template[2], "|", game_template[3], "|")
    print("|", game_template[4], "|", game_template[5], "|", game_template[6], "|")
    print("|", game_template[7], "|", game_template[8], "|", game_template[9], "|")
    print("-------------")

# This function replaces the game_template field with the char of the user/ computer
def active_game(xo):
    i = 0
    if xo == "X":
        input_computer = "O"
    else:
        input_computer = "X"

    while i < 9:
        show_game_template()
        input_gamer = input("Which field do you choose?:")
        input_gamer = int(input_gamer)

        # Users turn
        game_template[input_gamer] = xo
        print(input_gamer)
        list_of_numbers.remove(input_gamer)

        # computers turn
        number_computer = random.choice(list_of_numbers)
        game_template[number_computer] = input_computer
        list_of_numbers.remove(number_computer)


user_input = input("Hey user choose between X and O:").upper()
if user_input == "X" or user_input == "O":
    active_game(user_input)
else:
    print("Please enter a valid char.")
