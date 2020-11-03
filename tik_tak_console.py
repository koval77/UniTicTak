#new,fresh board
tictak_string="_________"
status=""



def draw_board(tictak):
    print("~~~~~~~~~")
    print(f'| {tictak_string[0]} {tictak[1]} {tictak[2]} |')
    print(f'| {tictak_string[3]} {tictak[4]} {tictak[5]} |')
    print(f'| {tictak_string[6]} {tictak[7]} {tictak[8]} |')
    print("~~~~~~~~~")


def result(tictak):
    global status
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
        status="Error"
        return 'This is impossible'
    elif (tictak[0] == 'O' and tictak[1] == 'O' and tictak[2] == 'O') or (
            tictak[3] == 'O' and tictak[4] == 'O' and tictak[5] == 'O') or (
            tictak[6] == 'O' and tictak[7] == 'O' and tictak[8] == 'O') or (
            tictak[0] == 'O' and tictak[3] == 'O' and tictak[6] == 'O') or (
            tictak[1] == 'O' and tictak[4] == 'O' and tictak[7] == 'O') or (
            tictak[2] == 'O' and tictak[5] == 'O' and tictak[8] == 'O') or (
            tictak[0] == 'O' and tictak[4] == 'O' and tictak[8] == 'O') or (
            tictak[2] == 'O' and tictak[4] == 'O' and tictak[6] == 'O'):
        status="ended"
        return "Player 'O' wins"
    elif (tictak[0] == 'X' and tictak[1] == 'X' and tictak[2] == 'X') or (
            tictak[3] == 'O' and tictak[4] == 'X' and tictak[5] == 'X') or (
            tictak[6] == 'X' and tictak[7] == 'X' and tictak[8] == 'X') or (
            tictak[0] == 'X' and tictak[3] == 'X' and tictak[6] == 'X') or (
            tictak[1] == 'X' and tictak[4] == 'X' and tictak[7] == 'X') or (
            tictak[2] == 'X' and tictak[5] == 'X' and tictak[8] == 'X') or (
            tictak[0] == 'X' and tictak[4] == 'X' and tictak[8] == 'X') or (
            tictak[2] == 'X' and tictak[4] == 'X' and tictak[6] == 'X'):
        status="ended"
        return "Player 'X' wins"
    for row in rows:
        # if row == ['X', 'X', 'X']:
        #     return "X wins"
        # elif row == ['O', 'O', 'O']:
        #     return "O wins"
        if row == row3 and (row != ['O', 'O', 'O'] and row != ['X', 'X', 'X']) and '_' in tictak:
            status="ongoing"
            return "The fight is still on"
        elif row == row3 and ('OOO' not in row and 'XXX' not in row) and '_' not in tictak:
            status="ended"
            return 'This would be a draw'

print("Let's the game begin!!!")
draw_board(tictak_string)
while status!="ended":
    print("Next player turn.")
    tictak_string = input()
    tictak_string = tictak_string.upper()
    draw_board(tictak_string)
    print(result(tictak_string))
# print(f'ilosc x:{tictak_string.count("X")}')
# print(f'ilosc o:{tictak_string.count("O")}')



