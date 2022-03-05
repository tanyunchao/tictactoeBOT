import random
import sys
import copy

player = ['O','X']

def main():

#     board = [
#   ['O', 'X', None],
#   [None, None, None],
#   ['X', 'O', None]
# ]
    # implementing command line arguements to select players
    if len(sys.argv) == 3:
        player_name = []
        for i in range(1, 3):
            player_name.append(sys.argv[i])
            # play is actually list of strings
        print('good to go')
    else:
        print('Invalid usage: python tic2.py <player 1> <player 2>')
        return 1


    # creates new board and renders it
    board = new_board()
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

        # set naming to BOT1 = random bot, BOT2 = Find_winning_moves, BOT3 = Find_win_prevent_loss, human = human_player
        while True:
            if N == 0:
                # player O (alw starts first)
                if player_name[0] == 'BOT1':
                    move_coords = random_ai(board, player[N])
                elif player_name[0] == 'BOT2':
                    move_coords = finds_winning_moves_ai(board, player[N])
                elif player_name[0] == 'BOT3':
                    move_coords = finds_winning_and_losing_moves_ai(board, player[N])
                elif player_name[0] == 'BOT4':
                    print("error BOT4 can only be used as player X aka second player")
                elif player_name[0] == 'human':
                    move_coords = human_player(board, player[N])
                
            elif N == 1:
                # player X
                if player_name[1] == 'BOT1':
                    move_coords = random_ai(board, player[N])
                elif player_name[1] == 'BOT2':
                    move_coords = finds_winning_moves_ai(board, player[N])
                elif player_name[1] == 'BOT3':
                    move_coords = finds_winning_and_losing_moves_ai(board, player[N])
                elif player_name[1] == 'BOT4':
                    move_coords = minimax_ai(board, player[N])
                elif player_name[1] == 'human':
                    move_coords = human_player(board, player[N])
            
            if is_valid_move(board, move_coords):
                break
            else:
                print("Invalid move, try again")

        board = make_move(board, move_coords, player[N])
        count += 1
        render(board)
        if get_winner(board) != None:
            if get_winner(board) == 1:
                print("game draw")
                return 1
            winner = get_winner(board)
            print("winner is player %s !" % winner)
            return 1

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
    print("")
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

    # test for draw:
    n_count = 0
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                n_count += 1
    if n_count == 0:
        return 1
    
    # game hasnt ended
    return None

def random_ai(board, player):
    move_set = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                move_set.append([y, x])
    end = len(move_set)
    # -1 as the move_set indexes from 0
    W = (random.randint(1, end) - 1)
    return move_set[W]

def finds_winning_moves_ai(board, player):
    # updating possible move sets
    move_set = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                move_set.append([y, x])
    end = len(move_set)
    
    # checking for winning play
    # horizontal check
    for y in range(3):
        count = 0 
        for x in range(3):
            if board[y][x] == player:
                count += 1
            if count == 2:
                # place to insert might not be same as postion y, x
                # need to reloop through row to make double confirm legal move
                for foo in range(3):
                    if [y, foo] in move_set:
                        return [y, foo]

    # vertical check
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] == player:
                count += 1
            if count == 2:
                for bar in range(3):
                    if [bar, x] in move_set:
                        return [bar, x]
    
    # diagonal check 1 eg [0, 0], [1, 1], [2, 2]
    count = 0
    for i in range(3):
        if board[i][i] == player:
            count += 1
    if count == 2:
        for K in range(3):
            if [K, K] in move_set:
                return [K, K]

    # diagonal check 2 eg [2, 0], [1, 1], [0, 2]
    count = 0
    diag = [[2, 0], [1, 1], [0, 2]] 
    for i in diag:
        y = i[0]
        x = i[1]
        if board[y][x] == player:
            count += 1
    if count == 2:
        for i in range(3):
            if diag[i] in move_set:
                return diag[i]

    

    # -1 as the move_set indexes from 0
    W = (random.randint(1, end) - 1)
    return move_set[W]    

def finds_winning_and_losing_moves_ai(board, player):
    # START of WINNING MOVES
    # updating possible move sets
    move_set = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                move_set.append([y, x])
    end = len(move_set)
    
    # checking for winning play
    # horizontal check
    for y in range(3):
        count = 0 
        for x in range(3):
            if board[y][x] == player:
                count += 1
            if count == 2:
                # place to insert might not be same as postion y, x
                # need to reloop through row to make double confirm legal move
                for foo in range(3):
                    if [y, foo] in move_set:
                        return [y, foo]

    # vertical check
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] == player:
                count += 1
            if count == 2:
                for bar in range(3):
                    if [bar, x] in move_set:
                        return [bar, x]
    
    # diagonal check 1 eg [0, 0], [1, 1], [2, 2]
    count = 0
    for i in range(3):
        if board[i][i] == player:
            count += 1
    if count == 2:
        for K in range(3):
            if [K, K] in move_set:
                return [K, K]

    # diagonal check 2 eg [2, 0], [1, 1], [0, 2]
    count = 0
    diag = [[2, 0], [1, 1], [0, 2]] 
    for i in diag:
        y = i[0]
        x = i[1]
        if board[y][x] == player:
            count += 1
    if count == 2:
        for i in range(3):
            if diag[i] in move_set:
                return diag[i]

    # START OF BLOCKING LOSING MOVES
    # SAME as WINNING MOVES BUT PLAYER TO LOOK OUT FOR CHANGE
    # checking for winning play
    # horizontal check
    for y in range(3):
        count = 0 
        for x in range(3):
            if board[y][x] != player and board[y][x] != None:
                count += 1
            if count == 2:
                # place to insert might not be same as postion y, x
                # need to reloop through row to make double confirm legal move
                for foo in range(3):
                    if [y, foo] in move_set:
                        return [y, foo]

    # vertical check
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] != player and board[y][x] != None:
                count += 1
            if count == 2:
                for bar in range(3):
                    if [bar, x] in move_set:
                        return [bar, x]
    
    # diagonal check 1 eg [0, 0], [1, 1], [2, 2]
    count = 0
    for i in range(3):
        if board[i][i] != player and board[i][i] != None:
            count += 1
    if count == 2:
        for K in range(3):
            if [K, K] in move_set:
                return [K, K]

    # diagonal check 2 eg [2, 0], [1, 1], [0, 2]
    count = 0
    diag = [[2, 0], [1, 1], [0, 2]] 
    for i in diag:
        y = i[0]
        x = i[1]
        if board[y][x] != player and board[y][x] != None:
            count += 1
    if count == 2:
        for i in range(3):
            if diag[i] in move_set:
                return diag[i]

    # START OF RANDOM MOVE
    # -1 as the move_set indexes from 0
    W = (random.randint(1, end) - 1)
    return move_set[W]    

def human_player(board, player):
    y = int(input("What is your move's Y co-coordinate?: "))
    x = int(input("What is your move's X co-coordinate?: "))
    move_coords = []
    move_coords.append(y)
    move_coords.append(x)
    print(move_coords)
    return move_coords

# minimax is hardcoded to work for player X only
def minimax_score(board, player):
    if get_winner(board) == 'X':
        return +10
    elif get_winner(board) == 'O':
        return -10
    elif get_winner(board) == 1:
        return 0

    # move_set is a list of list of possible moves
    move_set = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                move_set.append([y, x])
    
    # too lazy to build get opponent function
    # therefore built in
    if player == 'X':
        opponent = 'O'
    elif player =='O':
        opponent = 'X'

    scores = []
    for moves in move_set:
        # this step is actually changing the board
        # need to copy the board instead? yea cannot just copy list like that it is pointing to the same list
        state = copy.deepcopy(board)
        
        make_move(state, moves, player)
        score = minimax_score(state, opponent)
        scores.append(score)
    
    if player == 'X':
        return max(scores)
    
    if player == 'O':
        return min(scores)

def minimax_ai(board, player):
    best_move = None
    best_score = None

    # too lazy to build get opponent function
    # therefore built in
    if player == 'X':
        opponent = 'O'
    elif player =='O':
        opponent = 'X'

    # getting all legal moves
    move_set = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == None:
                move_set.append([y, x])
    
    for moves in move_set:
        # minimax_score returns best score of each board??
        _board = copy.deepcopy(board)
        make_move(_board, moves, player)
        score = minimax_score(_board, opponent)
        if best_score == None:
            best_score = score
            best_move = moves
        elif score > best_score:
            best_score = score
            best_move = moves
    # will return invalid move which prompts another move which will return none therefore null
    return best_move 


main()

