# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)


# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']

# display(row1, row2, row3)


def position_row():
    choice_list = [1, 2, 3]
    while True:
        try:
            choice_row = int(input('Choose a row: 1, 2, or 3 '))
            if choice_row not in choice_list:
                print('Warning! Invalid number')
                exit()
        except ValueError:
            print('Warning! Characters not allowed!')
            exit()
        return choice_row


number_row = position_row()


def new_position_row():
    choice_list = [1, 2, 3]


# def position_index():
#     choice_list = [1, 2, 3]
#     while True:
#         try:
#             choice_index = int(input('Choose an Index: 1, 2, or 3 '))
#             if choice_index not in choice_list:
#                 print('Warning! Invalid number')
#                 exit()
#         except ValueError:
#             print('Warning! Characters not allowed!')
#             exit()
#         return choice_index


# number_index = position_index()


# def main_():
#     while True:
#         if number_row == 1:
#             row1[number_index - 1] = 'X'
#             display(row1, row2, row3)
#             break
#         elif number_row == 2:
#             row2[number_index - 1] = 'X'
#             display(row1, row2, row3)
#             break
#         elif number_row == 3:
#             row3[number_index - 1] = 'X'
#             display(row1, row2, row3)
#             break


# main_()
