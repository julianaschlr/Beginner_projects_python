import random

game_template = [" ",
                 "1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = ""


# Function creates the template for the game
def show_game_template():
    print("-------------")
    print("|", game_template[1], "|", game_template[2], "|", game_template[3], "|")
    print("|", game_template[4], "|", game_template[5], "|", game_template[6], "|")
    print("|", game_template[7], "|", game_template[8], "|", game_template[9], "|")
    print("-------------")


def winning_combos():
    if game_template[1] == game_template[2] == game_template[3]:
        return game_template[1]
    elif game_template[4] == game_template[5] == game_template[6]:
        return game_template[4]
    elif game_template[7] == game_template[8] == game_template[9]:
        return game_template[7]
    elif game_template[1] == game_template[4] == game_template[7]:
        return game_template[1]
    elif game_template[2] == game_template[5] == game_template[8]:
        return game_template[2]
    elif game_template[3] == game_template[6] == game_template[9]:
        return game_template[3]
    elif game_template[1] == game_template[5] == game_template[9]:
        return game_template[1]
    elif game_template[7] == game_template[5] == game_template[3]:
        return game_template[7]
    else:
        print("Another round!")


# This function replaces the game_template field with the char of the user/ computer
def active_game(xo):
    i = ""
    if xo == "X":
        input_computer = "O"
    else:
        input_computer = "X"
    show_game_template()

    # this part replaces fields with chars and looks for winning combos
    while i != "X" and i != "O":
        input_gamer = input("Which field do you choose?:")
        try:
            input_gamer = int(input_gamer)
        except ValueError:
            print("Please enter a valid number!")
            continue
        if input_gamer in list_of_numbers:

            # Users turn
            game_template[input_gamer] = xo
            print(input_gamer)
            list_of_numbers.remove(input_gamer)

            # computers turn
            try:
                number_computer = random.choice(list_of_numbers)
                game_template[number_computer] = input_computer
                list_of_numbers.remove(number_computer)

            except IndexError:
                print("Okay there is no option for the computer left.")

        else:
            print("Your number isn't valid or you have already used it!")
            continue

        show_game_template()
        i = winning_combos()

    # Looks for the winner user or computer
    if i == "X" and xo == "X" or i == "O" and xo == "O":
        print("You win!")
        exit()
    else:
        print("You loose.")
        exit()


# user can choose between x and o and start game
def start_game(gamer_input):
    while user_input != "X" or user_input != "O":
        if user_input == "X" or user_input == "O":
            active_game(user_input)
        else:
            print("Please enter a valid char.")


user_input = input("Hey user choose between X and O:").upper()
start_game(user_input)
