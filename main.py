# CONVERT THE BOARDS FROM STRINGS LISTS
def convert_strings_to_list(board):
    board_list = list(board.split('\n'))
    return board_list


def is_valid_move(board, row, column, direction):
    if board[row][column] == '@':
        if direction == '1':
            if board[row - 1][column] == '@' and board[row - 2][column] == '-':
                return True
            else:
                return False

        if direction == '2':
            if row >= len(board) - 2:
                return False
            else:
                if board[row + 1][column] == '@' and board[row + 2][column] == '-':
                    return True
                else:
                    return False

        if direction == '3':
            if board[row][column - 1] == '@' and board[row][column - 2] == '-':
                return True
            else:
                return False

        if direction == '4':
            if column >= len(board[0]) - 2:
                return False
            else:
                if board[row][column + 1] == '@' and board[row][column + 2] == '-':
                    return True
                else:
                    return False


def perform_move(board, row, column, direction):
    if direction == '1':
        board[row] = board[row][:column] + '-' + board[row][column + 1:]
        board[row - 1] = board[row - 1][:column] + '-' + board[row - 1][column + 1:]
        board[row - 2] = board[row - 2][:column] + '@' + board[row - 2][column + 1:]
    elif direction == '2':
        board[row] = board[row][:column] + '-' + board[row][column + 1:]
        board[row + 1] = board[row + 1][:column] + '-' + board[row + 1][column + 1:]
        board[row + 2] = board[row + 2][:column] + '@' + board[row + 2][column + 1:]
    elif direction == '3':
        board[row] = board[row][:column] + '-' + board[row][column + 1:]
        board[row] = board[row][:column - 1] + '-' + board[row][column:]
        board[row] = board[row][:column - 2] + '@' + board[row][column - 1:]
    elif direction == '4':
        board[row] = board[row][:column] + '-' + board[row][column + 1:]
        board[row] = board[row][:column + 1] + '-' + board[row][column + 2:]
        board[row] = board[row][:column + 2] + '@' + board[row][column + 3:]
    return board


def count_pegs_remaining(board):
    n = 0
    for i in board:
        if i == '@':
            n += 1
    return n


def count_moves_available(board):
    n = 0
    for r in range(len(board)):
        for i in range(len(board[r])):
            if is_valid_move(board=req_board_list, row=r, column=i, direction='1'):
                n += 1
            if is_valid_move(board=req_board_list, row=r, column=i, direction='2'):
                n += 1
            if is_valid_move(board=req_board_list, row=r, column=i, direction='3'):
                n += 1
            if is_valid_move(board=req_board_list, row=r, column=i, direction='4'):
                n += 1
    return n


def direction_in_words(direction):
    d = ''
    if direction == '1':
        d += 'UP'
    elif direction == '2':
        d += 'DOWN'
    elif direction == '3':
        d += 'LEFT'
    elif direction == '4':
        d += 'RIGHT'
    return d


# ALL THE BOARDS IN STRING DATA TYPE
Cross = ' 123456789\n' \
        '1###@@@###\n' \
        '2###@@@###\n' \
        '3@@@@@@@@@\n' \
        '4@@@@-@@@@\n' \
        '5@@@@@@@@@\n' \
        '6###@@@###\n' \
        '7###@@@###'

Circle = ' 123456\n' \
         '1#-@@-#\n' \
         '2-@@@@-\n' \
         '3@@@@@@\n' \
         '4@@@@@@\n' \
         '5-@@@@-\n' \
         '6#-@@-#\n'

Triangle = ' 123456789\n' \
           '1###-@-###\n' \
           '2##-@@@-##\n' \
           '3#-@@-@@-#\n' \
           '4-@@@@@@@-\n'

Simple_T = ' 12345\n' \
           '1-----\n' \
           '2-@@@-\n' \
           '3--@--\n' \
           '4--@--\n' \
           '5-----'

boards_list = [Cross, Circle, Triangle, Simple_T]

# GENERAL LAYOUT OF THE GAME
print('WELCOME TO PEG SOLITAIRE!')
print('===============================')

print('Board Style Menu\n'
      '\t1) Cross\n'
      '\t2) Circle\n'
      '\t3) Triangle\n'
      '\t4) Simple T\n')

# TAKE THE INPUT FOR THE TYPE OF BOARD
t = 1
while t == 1:
    board_style = int(input('Choose a board style: '))
    req_board = boards_list[board_style - 1]
    req_board_list = convert_strings_to_list(req_board)

    if 1 <= board_style <= 4:
        print(req_board)
        t = 0

    else:
        print('Please enter your choice as an integer between 1 and 4')

# no_of_moves_left = count_moves_available(req_board_list)
# print(number_of_moves_left)
# TAKE THE INPUT FOR WHICH PEG TO MOVE
x = True
while x:
    # count_moves_available(req_board_list)
    while True:
        peg_column = int(input("Choose the COLUMN of a peg you'd like to move: "))
        if peg_column <= len(req_board_list[0]) - 1:
            break
        else:
            print(f'Please enter your choice as an integer between 1 and {len(req_board_list[0]) - 1}: ')
    while True:
        peg_row = int(input("Choose the ROW of a peg you'd like to move: "))
        if peg_row <= len(req_board_list) - 1:
            break
        else:
            print(f'Please enter your choice as an integer between 1 and {len(req_board_list) - 1}: ')
    while True:
        peg_direction = input('Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: ')
        if peg_direction in '1234':
            break
        else:
            print('Please enter your choice as an integer between 1 and 4: ')

    if is_valid_move(board=req_board_list, row=peg_row, column=peg_column, direction=peg_direction):
        req_board_list = perform_move(board=req_board_list, row=peg_row, column=peg_column, direction=peg_direction)
        req_board = '\n'.join(req_board_list)
        print(req_board)
    else:
        Direction = direction_in_words(peg_direction)
        print(f'Moving a peg from row {peg_row} and column {peg_column} {Direction} is not currently a legal move.')
        print(req_board)

    if count_pegs_remaining(req_board) == 1:
        print('Congrats, you won!')
        break
    if count_moves_available(req_board_list) < 1 < count_pegs_remaining(req_board):
        print('It looks like there are no more legal moves.  Please try again.')
        x = False

print('==========================================')
print('THANK YOU FOR PLAYING PEG SOLITAIRE!')
