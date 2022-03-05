player = ['O','X']
def main():
    board = new_board()
    # board[0][1] = 'O'
    # board[1][1] = 'X'
    # board[2][0] = 'X'
    # board[2][1] = 'X'
    # board[2][2] = 'O'
    print(board)
    render(board)

    count = 0
    while count < 9:
        if count == 0:
            N = 0 
        elif (count % 2) != 0:
            N = 1
        elif (count % 2) == 0:
            N = 0
        move_coords = None
        while True:
            move_coords = get_move()
            if is_valid_move(board, move_coords):
                break
            else:
                print("Invalid move, try again")

        board = make_move(board, move_coords, player[N])
        count += 1
        render(board)
        if get_winner(board) != None:
            winner = get_winner(board)
            print("winner is player %s !" % winner)
            return winner
        
    print("Game draw")
    


def new_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(None)
        board.append(row)
        
    return board

def render(board):
    # top row formatting
    print("  0 1 2")
    print("  ------")

    # insert printing of first row of board
        # if first two characters in row print " "
    for i in range(3):
        print(f"%i|" % (i), end ='')
        for j in range(3):
            # set to print ' ' instead of none so board looks correct
            if board[i][j] == None:
                print(" ", end = '')
            else:
                print(board[i][j], end = '')

            if j < 2:
                print(" ", end = '')
            elif j == 2:
                print("|")

    print("  ------")
    return None

def get_move():
    y = int(input("What is your move's Y co-coordinate?: "))
    x = int(input("What is your move's X co-coordinate?: "))
    move_coords = []
    move_coords.append(y)
    move_coords.append(x)
    print(move_coords)
    return move_coords

def make_move(board, move_coords, player):
    # x and y coordinates to update respectively
    y = move_coords[0]
    x = move_coords[1]
    # since player is alr str either 'x' or 'y'
    # update and return board
    board[y][x] = player
    return board

def is_valid_move(board, move_coords):
    y = move_coords[0]
    x = move_coords[1]

    if x < 0 or x > 2:
        return False
    if y < 0 or y > 2:
        return False    

    if board[y][x] == None:
        return True
    else:
        return False

def get_winner(board):

    # test all horizontal rows
    # testing per row first
    for y in range(3):
        count = 0
        test = board[y][0]
        for x in range(1, 3):
            if test == board[y][x]:
                count += 1
        if count == 2:
            return test

    # test vertical rows
    for x in range(3):
        count = 0
        test = board[0][x]
        for y in range(1, 3):
            if test == board[y][x]:
                count += 1
        if count == 2:
            return test

    # test diagonal 1
    test = board[0][0]
    count = 0
    for x in range(1, 3):
        if test == board[x][x]:
            count += 1
    if count == 2:
        return test

    # test diagonal 2
    test = board[2][0]
    count = 0
    if test == board[1][1]:
        count += 1
    if test == board[0][2]:
        count += 1
    if count == 2:
        return test

    return None
        
main()
