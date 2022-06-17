from IPython.display import clear_output


def display_game(game_list):
    print("Here is the current list")
    print(game_list)


def position_choice():
    choice = 'wrong'
    valid_integers = ['0', '1', '2', ]
    while choice not in valid_integers:
        choice = input("Pick a position to replace (0,1,2) ")
        if choice not in valid_integers:
            print("Sorry, but you did not choose a valid position (0,1,2)")

    return int(choice)


def replacement_choice(game_list, position):
    string_placement = input("Type a string to replace at the position ")
    game_list[position] = string_placement

    return game_list


def gameon_choice():
    choice = 'WRONG'
    acceptable_choice = ['Y', 'N']
    while choice not in acceptable_choice:
        choice = input("Would you like to keep playing? Y or N. ")
        if choice not in acceptable_choice:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice == 'Y':
        return True
    else:
        return False


def start_game():
    game_on = True
    game_list = [0, 1, 2]

    while game_on:
        display_game(game_list)
        position = position_choice()
        game_list = replacement_choice(game_list, position)
        display_game(game_list)
        game_on = gameon_choice()


start_game()
# Warm Up Project Exercises

# Function to Display Information


# def display_list(my_list):
#     print(my_list)


# my_list = list(range(0, 11))
# # display_list(my_list)

# # Accepting User Input


# def user_choice():
#     '''
#     User inputs a number (0-10) and we return this in integer form.
#     No parameter is passed when calling this function.
#     '''

#     # This original choice value can be anything that isn't an integer
#     choice = 'Wrong'

#     # While the choice is not a digit, keep asking for input.
#     while choice.isdigit() == False:

#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input('Please enter a number (0-10): ')

#         # Error Message Check
#         if choice.isdigit() == False:
#             clear_output()
#             print("Sorry, but you did not enter an integer. Please try again.")

#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)


# # More Flexible Example


# # def user_choice():
# #     choice = 'Wrong'
# #     within_range = False

# #     while choice.isdigit() == False or within_range == False:

# #         choice = input('Please enter a number (0-10): ')

# #         if choice.isdigit() == False:
# #             print("Sorry that is not a digit")

# #         if choice.isdigit() == True:
# #             if int(choice) in range(0, 10):
# #                 within_range == True
# #             else:
# #                 within_range = False

# #     return int(choice)


# # user_choice()


# def user_choice():

#     choice = 'WRONG'
#     within_range = False

#     while choice.isdigit() == False or within_range == False:

#         choice = input("Please enter a number (0-10): ")

#         if choice.isdigit() == False:
#             print("Sorry that is not a digit!")

#         if choice.isdigit() == True:
#             if int(choice) in range(0, 10):
#                 within_range = True
#             else:
#                 within_range = False

#     return int(choice)


# def user_choice():
#     choice = 'WRONG'
#     within_range = str(range(0, 10))

#     while choice not in within_range:
#         choice = input("Please enter a number (0-10): ")

#         if choice not in within_range:
#             print("Sorry, Invalid choice!")

#     return int(choice)


# def position_choice():
#     choice = 'wrong'
#     acceptable_range = ['0', '1', '2']
#     while choice not in acceptable_range:
#         choice = input('Picka a position (0,1,2): ')
#         if choice not in acceptable_range:
#             print('Sorry, invalid choice')

#     return int(choice)


# Simple User Interaction
