
def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


def position_choice():
    choice = 'wrong'
    acceptable_range = ['0', '1', '2']
    while choice not in acceptable_range:
        choice = input('Picka a position (0,1,2): ')
        if choice not in acceptable_range:
            print('Sorry, invalid choice')

    return int(choice)


def replacement_choice(list, num):
    user_placement = input('Type a string to place at position ')
    list[num] = user_placement

    return list


def gameon_choice():
    choice = 'wrong'
    acceptable_choice = ['Y', 'N']
    while choice not in acceptable_choice:
        choice = input('Keep playing (Y or N): ')
        if choice not in acceptable_choice:
            print('Sorry, I dont understand, please choose Y or N')

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
