import numpy as np
import copy
import random
        
def get_score(piece):
    if piece[2] == 'p':
        return 5
    elif piece[2] == 'h':
        return 20
    elif piece[2] == 'b':
        return 30
    elif piece[2] == 'r':
        return 40
    elif piece[2] == 'q':
        return 100
    elif piece[2] == 'k':
        return 900
    else:
        return 0

# initialize chess board     
def initialize_board():
    board = []
    for i in range(8):
        if i == 0:
            row = []
            row.append('b-r')
            row.append('b-h')
            row.append('b-b')
            row.append('b-q')
            row.append('b-k')
            row.append('b-b')
            row.append('b-h')
            row.append('b-r')
            board.append(row)
            
        elif i == 1:
            row = []
            for k in range(8):
                row.append('b-p')
            board.append(row)
            
        elif i == 6:
            row = []
            for k in range(8):
                row.append('w-p')
            board.append(row)
            
        elif i == 7:
            row = []
            row.append('w-r')
            row.append('w-h')
            row.append('w-b')
            row.append('w-q')
            row.append('w-k')
            row.append('w-b')
            row.append('w-h')
            row.append('w-r')
            board.append(row)
            
        else:
            row = []
            for k in range(8):
                row.append('...')
            board.append(row)
    
    return board


# check if move is valid
def get_valid_moves(board, start_x, start_y):
    block = board[start_y][start_x]
    block_color = block[0]
    possible_moves = []
    
    # check for pawn
    if block[2] == 'p':
        
        # check for white pawn
        if block_color == 'w':
            if start_y != 0:
                if board[start_y-1][start_x][0] == '.':
                    possible_moves.append([start_x, start_y, start_x, start_y-1])
                    
                    if start_y == 6 and board[start_y-2][start_x][0] == '.':
                        possible_moves.append([start_x, start_y, start_x, start_y-2])
                
                if start_x < 7:        
                    if board[start_y-1][start_x+1][0] == 'b':
                        possible_moves.append([start_x, start_y, start_x+1, start_y-1])
                 
                if start_x > 0:   
                    if board[start_y-1][start_x-1][0] == 'b':
                        possible_moves.append([start_x, start_y, start_x-1, start_y-1])
        
        # check for black pawn                
        if block_color == 'b':
            if start_y != 7:
                if board[start_y+1][start_x][0] == '.':
                    possible_moves.append([start_x, start_y, start_x, start_y+1])

                    if start_y == 1 and board[start_y+2][start_x][0] == '.':
                        possible_moves.append([start_x, start_y, start_x, start_y+2])

                if start_x < 7:
                    if board[start_y+1][start_x+1][0] == 'w':
                        possible_moves.append([start_x, start_y, start_x+1, start_y+1])

                if start_x > 0:
                    if board[start_y+1][start_x-1][0] == 'w':
                        possible_moves.append([start_x, start_y, start_x-1, start_y+1])
                
    # check for horse
    if block[2] == 'h':
        # move 1 - right up
        if start_x + 2 <= 7 and start_y - 1 >= 0:
            if board[start_y-1][start_x+2][0] != block_color:
                possible_moves.append([start_x, start_y, start_x+2, start_y-1])
        
        # move 2 - right down
        if start_x + 2 <= 7 and start_y + 1 <= 7:
            if board[start_y+1][start_x+2][0] != block_color:
                possible_moves.append([start_x, start_y, start_x+2, start_y+1])
        
        # move 3 - left up 
        if start_x - 2 >= 0 and start_y - 1 >= 0:
            if board[start_y-1][start_x-2][0] != block_color:
                possible_moves.append([start_x, start_y, start_x-2, start_y-1])
        
        # move 4 - left down
        if start_x - 2 >= 0 and start_y + 1 <= 7:
            if board[start_y+1][start_x-2][0] != block_color:
                possible_moves.append([start_x, start_y, start_x-2, start_y+1])
                
        # move 5 - up left
        if start_x - 1 >= 0 and start_y - 2 >= 0:
            if board[start_y-2][start_x-1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y-2])
        
        # move 6 - up right
        if start_x + 1 <= 7 and start_y - 2 >= 0:
            if board[start_y-2][start_x+1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y-2])
        
        # move 7 - down left
        if start_x - 1 >= 0 and start_y + 2 <= 7:
            if board[start_y+2][start_x-1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y+2])
        
        # move 8 - down right
        if start_x + 1 <= 7 and start_y + 2 <= 7:
            if board[start_y+2][start_x+1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y+2])
    
    
    # check for rook or queen - queen and rook shares the same horizontal and vertical moves
    if block[2] == 'r' or block[2] == 'q':
        # check right
        temp_x = start_x
        while True:
            temp_x += 1
            if temp_x > 7:
                break
            if board[start_y][temp_x][0] == block_color:
                break
            if board[start_y][temp_x][0] != block_color and board[start_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, start_y])
                break
            possible_moves.append([start_x, start_y, temp_x, start_y])
            
        # check left
        temp_x = start_x
        while True:
            temp_x -= 1
            if temp_x < 0:
                break
            if board[start_y][temp_x][0] == block_color:
                break
            if board[start_y][temp_x][0] != block_color and board[start_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, start_y])
                break
            possible_moves.append([start_x, start_y, temp_x, start_y])
            
        # check up
        temp_y = start_y
        while True:
            temp_y -= 1
            if temp_y < 0:
                break
            if board[temp_y][start_x][0] == block_color:
                break
            if board[temp_y][start_x][0] != block_color and board[temp_y][start_x][0] != '.':
                possible_moves.append([start_x, start_y, start_x, temp_y])
                break
            possible_moves.append([start_x, start_y, start_x, temp_y])
        
        # check down
        temp_y = start_y
        while True:
            temp_y += 1
            if temp_y > 7:
                break
            if board[temp_y][start_x][0] == block_color:
                break
            if board[temp_y][start_x][0] != block_color and board[temp_y][start_x][0] != '.':
                possible_moves.append([start_x, start_y, start_x, temp_y])
                break
            possible_moves.append([start_x, start_y, start_x, temp_y])
    
    # check for bishop and queen - queen and bishop shares the same diagonal moves
    if block[2] == 'b' or block[2] == 'q':
        # check up right
        temp_y = start_y
        temp_x = start_x 
        while True:
            temp_y -= 1
            temp_x += 1
            if temp_y < 0 or temp_x > 7:
                break
            if board[temp_y][temp_x][0] == block_color:
                break
            if board[temp_y][temp_x][0] != block_color and board[temp_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, temp_y])
                break
            possible_moves.append([start_x, start_y, temp_x, temp_y])
        
        # check up left
        temp_y = start_y
        temp_x = start_x 
        while True:
            temp_y -= 1
            temp_x -= 1
            if temp_y < 0 or temp_x < 0:
                break
            if board[temp_y][temp_x][0] == block_color:
                break
            if board[temp_y][temp_x][0] != block_color and board[temp_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, temp_y])
                break
            possible_moves.append([start_x, start_y, temp_x, temp_y])
        
        # check down right
        temp_y = start_y
        temp_x = start_x
        while True:
            temp_y += 1
            temp_x += 1
            if temp_y > 7 or temp_x > 7:
                break
            if board[temp_y][temp_x][0] == block_color:
                break
            if board[temp_y][temp_x][0] != block_color and board[temp_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, temp_y])
                break
            possible_moves.append([start_x, start_y, temp_x, temp_y])
        
        # check down left
        temp_y = start_y
        temp_x = start_x
        while True:
            temp_y += 1
            temp_x -= 1
            if temp_y > 7 or temp_x < 0:
                break
            if board[temp_y][temp_x][0] == block_color:
                break
            if board[temp_y][temp_x][0] != block_color and board[temp_y][temp_x][0] != '.':
                possible_moves.append([start_x, start_y, temp_x, temp_y])
                break
            possible_moves.append([start_x, start_y, temp_x, temp_y])
            
    # check for king
    if block[2] == 'k':
        # check up
        if start_y - 1 >= 0:
            if board[start_y-1][start_x][0] != block_color:
                possible_moves.append([start_x, start_y, start_x, start_y-1])
                
            # check up right
            if start_x + 1 <= 7:
                if board[start_y-1][start_x+1][0] != block_color:
                    possible_moves.append([start_x, start_y, start_x+1, start_y-1])
                    
            # check up left
            if start_x - 1 >= 0:
                if board[start_y-1][start_x-1][0] != block_color:
                    possible_moves.append([start_x, start_y, start_x-1, start_y-1])
            
        # check down
        if start_y + 1 <= 7:
            if board[start_y+1][start_x][0] != block_color:
                possible_moves.append([start_x, start_y, start_x, start_y+1])
                
            # check down right
            if start_x + 1 <= 7:
                if board[start_y+1][start_x+1][0] != block_color:
                    possible_moves.append([start_x, start_y, start_x+1, start_y+1])
                    
            # check down left
            if start_x - 1 >= 0:
                if board[start_y+1][start_x-1][0] != block_color:
                    possible_moves.append([start_x, start_y, start_x-1, start_y+1])
        
        # check right
        if start_x + 1 <= 7:
            if board[start_y][start_x+1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y])
        
        # check left
        if start_x - 1 >= 0:
            if board[start_y][start_x-1][0] != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y])
    
    return possible_moves


# obtain all possible next moves
def get_all_possible_moves(board, color):
    all_possible_moves = []
    for i in range(8):
        for k in range(8):
            if board[i][k][0] == color:
                all_possible_moves.extend(get_valid_moves(board, k, i))         
    return all_possible_moves       


# make the transition for the move
def make_move(board, move):
    new_board = copy.deepcopy(board)
    start_x = move[0]
    start_y = move[1]
    end_x = move[2]
    end_y = move[3]
    
    new_board[end_y][end_x] = board[start_y][start_x]
    new_board[start_y][start_x] = '...'
    
    return new_board
    
    
# calculates heuristic based on white and black score
def calculate_score(board):
    white_score = 0
    black_score = 0
    
    for i in range(8):
        for k in range(8):
            block = board[i][k]
            if block[0] == 'w':
                white_score += get_score(block)
            elif block[0] == 'b':
                black_score += get_score(block)

    return white_score - black_score     


# perform heuristic calculation at a depth of 3
def heuristic(board, depth, mode, a_cutoff, b_cutoff):
    # MAX node - initialize with -infinity
    if mode == 'MAX':
        best_score = -100000000000
        color = 'w'
        
    # MIN node - initialize with +infinity
    else:
        best_score = 100000000000
        color = 'b'
        
    all_possible_moves = get_all_possible_moves(board, color)
    best_move = all_possible_moves[0]
    
    for new_move in all_possible_moves:
        
        new_board = make_move(board, new_move)
        
        if mode == 'MAX':
            next_mode = 'MIN'
        else:
            next_mode = 'MAX'
            
        new_score = 0
        
        # base case
        if depth == 1:
            new_score = calculate_score(new_board)
        else:
            _, new_score = heuristic(new_board, depth - 1, next_mode, a_cutoff, b_cutoff)
        
        if mode == 'MAX':
            if depth == 4 and new_score == best_score:
                print("new move: ", new_move)
            
            if new_score >= best_score:
                best_score = new_score
                best_move = new_move   
                a_cutoff = best_score
                
                # prune search tree
                if a_cutoff >= b_cutoff:
                    return best_move, b_cutoff + 1
                
        else:
            if new_score <= best_score:
                best_score = new_score
                best_move = new_move 
                b_cutoff = best_score
                
                # prune search tree
                if b_cutoff <= a_cutoff:
                    return best_move, a_cutoff - 1
                
    return best_move, best_score
        

# convert opponent move to list
def convert_move(op_move):
    opponent_move = []
    opponent_move.append(int(op_move[1]))
    opponent_move.append(int(op_move[4]))
    opponent_move.append(int(op_move[7]))
    opponent_move.append(int(op_move[10]))
    
    return opponent_move


# print board
def print_board(board):
    printed_board = [["0", "-0-", "-1-", "-2-", "-3-", "-4-", "-5-", "-6-", "-7-"]]
    for i in range(8):
        row = [i]
        row.extend(board[i])
        printed_board.append(row)
        
    print(np.array(printed_board))
    
            
if __name__ == "__main__":
    counter = 0
    board = initialize_board()
    
    print("move", counter, ": ")
    print_board(board)
    print()
    
    while True:
        play_mode = input("use bot? (y/n): ")
        if play_mode == 'y':
            opponent_move, best_score = heuristic(board, 4, 'MAX', -100000000000, 100000000000)
            print("best_score: ", best_score)
        else:
            op_move = input("Enter your move: ")
            opponent_move = convert_move(op_move)
            
        board = make_move(board, opponent_move)
        counter += 1
        print("white - move", counter, ": ")
        print_board(board)
        print()
        
        play_mode = input("use bot? (y/n): ")
        if play_mode == 'y':
            opponent_move, best_score = heuristic(board, 4, 'MIN', -100000000000, 100000000000)
            print("best_score: ", best_score)
        else:
            op_move = input("Enter your move: ")
            opponent_move = convert_move(op_move)

        board = make_move(board, opponent_move)
        counter += 1
        print("black - move", counter, ": ")
        print_board(board)
        print()
        
    
    
