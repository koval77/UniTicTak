# write your code here
print("Enter cells: > ")
tictak_string = input()
ind = 0
#tictak_string = ("O--X-----")
tictak_string = tictak_string.upper()


def draw_board(tictak):
    print("---------")
    print(f'| {tictak_string[0]} {tictak[1]} {tictak[2]} |')
    print(f'| {tictak_string[3]} {tictak[4]} {tictak[5]} |')
    print(f'| {tictak_string[6]} {tictak[7]} {tictak[8]} |')
    print("---------")


def result(tictak):
    row1 = [tictak[0], tictak[1], tictak[2]]
    row2 = [tictak[3], tictak[4], tictak[5]]
    row3 = [tictak[6], tictak[7], tictak[8]]
    rows = [row1, row2, row3]
    column1 = [tictak[0], tictak[3], tictak[6]]
    column2 = [tictak[1], tictak[4], tictak[7]]
    column3 = [tictak[2], tictak[5], tictak[8]]
    columns = [column1, column2, column3]
    if (['O', 'O', 'O'] in rows and ['X', 'X', 'X'] in rows) or (
            ['O', 'O', 'O'] in columns and ['X', 'X', 'X'] in columns) or (
            tictak.count('X') - tictak.count('O') >= 2) or (tictak.count(
        'O') - tictak.count('X') >= 2):
        return 'Impossible'
    elif (tictak[0] == 'O' and tictak[1] == 'O' and tictak[2] == 'O') or (
            tictak[3] == 'O' and tictak[4] == 'O' and tictak[5] == 'O') or (
            tictak[6] == 'O' and tictak[7] == 'O' and tictak[8] == 'O') or (
            tictak[0] == 'O' and tictak[3] == 'O' and tictak[6] == 'O') or (
            tictak[1] == 'O' and tictak[4] == 'O' and tictak[7] == 'O') or (
            tictak[2] == 'O' and tictak[5] == 'O' and tictak[8] == 'O') or (
            tictak[0] == 'O' and tictak[4] == 'O' and tictak[8] == 'O') or (
            tictak[2] == 'O' and tictak[4] == 'O' and tictak[6] == 'O'):
        return "O wins"
    elif (tictak[0] == 'X' and tictak[1] == 'X' and tictak[2] == 'X') or (
            tictak[3] == 'O' and tictak[4] == 'X' and tictak[5] == 'X') or (
            tictak[6] == 'X' and tictak[7] == 'X' and tictak[8] == 'X') or (
            tictak[0] == 'X' and tictak[3] == 'X' and tictak[6] == 'X') or (
            tictak[1] == 'X' and tictak[4] == 'X' and tictak[7] == 'X') or (
            tictak[2] == 'X' and tictak[5] == 'X' and tictak[8] == 'X') or (
            tictak[0] == 'X' and tictak[4] == 'X' and tictak[8] == 'X') or (
            tictak[2] == 'X' and tictak[4] == 'X' and tictak[6] == 'X'):
        return "X wins"
    for row in rows:
        if row == row3 and (row != ['O', 'O', 'O'] and row != ['X', 'X', 'X']) and '_' in tictak:
            return "Game not finished"
        elif row == row3 and ('OOO' not in row and 'XXX' not in row) and '_' not in tictak:
            return 'Draw'


def validate_coordinates(coordinates):
    global tictak_string
    translate_co(coordinates[0], coordinates[1])
    if not (coordinates[0].isnumeric() and coordinates[1].isnumeric()):
        print("You should enter numbers!")
        ask_for_coordinates()
    elif (int(coordinates[0]) < 1 or int(coordinates[0]) > 3) or (int(coordinates[1]) < 1 or int(coordinates[1]) > 3):
        print("Coordinates should be from 1 to 3!")
        ask_for_coordinates()
    elif tictak_string[ind] == 'O' or tictak_string[ind] == 'X':
        print("This cell is occupied! Choose another one!")
        ask_for_coordinates()
    else:
        #tictak_string_list=tictak_string.split("")
        tictak_string_list=[char for char in tictak_string]
        tictak_string_list[ind]='X'
        tictak_string="".join(tictak_string_list)


def translate_co(x, y):
    global ind
    i = int(x)
    j = int(y)
    if [i, j] == [1, 1]:
        ind = 6
    elif [i, j] == [1, 2]:
        ind = 3
    elif [i, j] == [1, 3]:
        ind = 0
    elif [i, j] == [2, 1]:
        ind = 7
    elif [i, j] == [2, 2]:
        ind = 4
    elif [i, j] == [2, 3]:
        ind = 1
    elif [i, j] == [3, 1]:
        ind = 8
    elif [i, j] == [3, 2]:
        ind = 5
    elif [i, j] == [3, 3]:
        ind = 2

def ask_for_coordinates():
    print("Enter the coordinates: > ")
    coordinates_list = [x for x in input().split()]
    validate_coordinates(coordinates_list)

draw_board(tictak_string)
print(result(tictak_string))
ask_for_coordinates()
# print(coordinates_list[0].isnumeric())
draw_board(tictak_string)
