import numpy as np
import copy

class Block:
    def __init__(self, symbol, color):
        self.color = color
        self.type = symbol
        
    def is_empty(self):
        return self.type == '.'
        
    def is_pawn(self):
        return self.type == 'p'
    
    def is_horse(self):
        return self.type == 'h'
    
    def is_bishop(self):
        return self.type == 'b'
    
    def is_rook(self):
        return self.type =='r'
    
    def is_queen(self):
        return self.type == 'q'
    
    def is_king(self):
        return self.type == 'k'
    
    def __repr__(self):
        return self.type
    
    def get_color(self):
        return self.color
    
    def get_score(self):
        if self.is_pawn():
            return 1
        elif self.is_horse():
            return 3
        elif self.is_bishop():
            return 3
        elif self.is_rook():
            return 5
        elif self.is_queen():
            return 10
        elif self.is_king():
            return 50
        else:
            return 0      

# initialize chess board     
def initialize_board():
    board = []
    for i in range(8):
        if i == 0:
            row = []
            row.append(Block('r', 'black'))
            row.append(Block('h', 'black'))
            row.append(Block('b', 'black'))
            row.append(Block('q', 'black'))
            row.append(Block('k', 'black'))
            row.append(Block('b', 'black'))
            row.append(Block('h', 'black'))
            row.append(Block('r', 'black'))
            board.append(row)
            
        elif i == 1:
            row = []
            for k in range(8):
                row.append(Block('p', 'black'))
            board.append(row)
            
        elif i == 6:
            row = []
            for k in range(8):
                row.append(Block('p', 'white'))
            board.append(row)
            
        elif i == 7:
            row = []
            row.append(Block('r', 'white'))
            row.append(Block('h', 'white'))
            row.append(Block('b', 'white'))
            row.append(Block('q', 'white'))
            row.append(Block('k', 'white'))
            row.append(Block('b', 'white'))
            row.append(Block('h', 'white'))
            row.append(Block('r', 'white'))
            board.append(row)
            
        else:
            row = []
            for k in range(8):
                block = Block('.', 'none')
                row.append(block)
            board.append(row)
    
    return board


# check if move is valid
def get_valid_moves(board, start_x, start_y):
    block = board[start_y][start_x]
    block_color = block.get_color()
    possible_moves = []
    
    # check for pawn
    if block.is_pawn():
        
        # check for white pawn
        if block_color == 'white':
            if start_y != 0:
                if board[start_y-1][start_x].is_empty():
                    possible_moves.append([start_x, start_y, start_x, start_y-1])
                    
                    if start_y == 6 and board[start_y-2][start_x].is_empty():
                        possible_moves.append([start_x, start_y, start_x, start_y-2])
                
                if start_x < 7:        
                    if board[start_y-1][start_x+1].get_color() == 'black':
                        possible_moves.append([start_x, start_y, start_x+1, start_y-1])
                 
                if start_x > 0:   
                    if board[start_y-1][start_x-1].get_color() == 'black':
                        possible_moves.append([start_x, start_y, start_x-1, start_y-1])
        
        # check for black pawn                
        if block_color == 'black':
            if start_y != 7:
                if board[start_y+1][start_x].is_empty():
                    possible_moves.append([start_x, start_y, start_x, start_y+1])

                    if start_y == 1 and board[start_y+2][start_x].is_empty():
                        possible_moves.append([start_x, start_y, start_x, start_y+2])

                if start_x < 7:
                    if board[start_y+1][start_x+1].get_color() == 'white':
                        possible_moves.append([start_x, start_y, start_x+1, start_y+1])

                if start_x > 0:
                    if board[start_y+1][start_x-1].get_color() == 'white':
                        possible_moves.append([start_x, start_y, start_x-1, start_y+1])
                
    # check for horse
    if block.is_horse():
        # move 1 - right up
        if start_x + 2 <= 7 and start_y - 1 >= 0:
            if board[start_y-1][start_x+2].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x+2, start_y-1])
        
        # move 2 - right down
        if start_x + 2 <= 7 and start_y + 1 <= 7:
            if board[start_y+1][start_x+2].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x+2, start_y+1])
        
        # move 3 - left up 
        if start_x - 2 >= 0 and start_y - 1 >= 0:
            if board[start_y-1][start_x-2].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x-2, start_y-1])
        
        # move 4 - left down
        if start_x - 2 >= 0 and start_y + 1 <= 7:
            if board[start_y+1][start_x-2].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x-2, start_y+1])
                
        # move 5 - up left
        if start_x - 1 >= 0 and start_y - 2 >= 0:
            if board[start_y-2][start_x-1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y-2])
        
        # move 6 - up right
        if start_x + 1 <= 7 and start_y - 2 >= 0:
            if board[start_y-2][start_x+1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y-2])
        
        # move 7 - down left
        if start_x - 1 >= 0 and start_y + 2 <= 7:
            if board[start_y+2][start_x-1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y+2])
        
        # move 8 - down right
        if start_x + 1 <= 7 and start_y + 2 <= 7:
            if board[start_y+2][start_x+1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y+2])
    
    
    # check for rook or queen - queen and rook shares the same horizontal and vertical moves
    if block.is_rook() or block.is_queen():
        # check right
        temp_x = start_x
        while True:
            temp_x += 1
            if temp_x > 7:
                break
            if board[start_y][temp_x].get_color() == block_color:
                break
            if board[start_y][temp_x].get_color() != block_color and board[start_y][temp_x].get_color != 'none':
                possible_moves.append([start_x, start_y, temp_x, start_y])
                break
            possible_moves.append([start_x, start_y, temp_x, start_y])
            
        # check left
        temp_x = start_x
        while True:
            temp_x -= 1
            if temp_x < 0:
                break
            if board[start_y][temp_x].get_color() == block_color:
                break
            if board[start_y][temp_x].get_color() != block_color and board[start_y][temp_x].get_color != 'none':
                possible_moves.append([start_x, start_y, temp_x, start_y])
                break
            possible_moves.append([start_x, start_y, temp_x, start_y])
            
        # check up
        temp_y = start_y
        while True:
            temp_y -= 1
            if temp_y < 0:
                break
            if board[temp_y][start_x].get_color() == block_color:
                break
            if board[temp_y][start_x].get_color() != block_color and board[temp_y][start_x].get_color != 'none':
                possible_moves.append([start_x, start_y, start_x, temp_y])
                break
            possible_moves.append([start_x, start_y, start_x, temp_y])
        
        # check down
        temp_y = start_y
        while True:
            temp_y += 1
            if temp_y > 7:
                break
            if board[temp_y][start_x].get_color() == block_color:
                break
            if board[temp_y][start_x].get_color() != block_color and board[temp_y][start_x].get_color != 'none':
                possible_moves.append([start_x, start_y, start_x, temp_y])
                break
            possible_moves.append([start_x, start_y, start_x, temp_y])
    
    # check for bishop and queen - queen and bishop shares the same diagonal moves
    if block.is_bishop() or block.is_queen():
        # check up right
        temp_y = start_y
        temp_x = start_x 
        while True:
            temp_y -= 1
            temp_x += 1
            if temp_y < 0 or temp_x > 7:
                break
            if board[temp_y][temp_x].get_color() == block_color:
                break
            if board[temp_y][temp_x].get_color() != block_color and board[temp_y][temp_x].get_color != 'none':
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
            if board[temp_y][temp_x].get_color() == block_color:
                break
            if board[temp_y][temp_x].get_color() != block_color and board[temp_y][temp_x].get_color != 'none':
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
            if board[temp_y][temp_x].get_color() == block_color:
                break
            if board[temp_y][temp_x].get_color() != block_color and board[temp_y][temp_x].get_color != 'none':
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
            if board[temp_y][temp_x].get_color() == block_color:
                break
            if board[temp_y][temp_x].get_color() != block_color and board[temp_y][temp_x].get_color != 'none':
                possible_moves.append([start_x, start_y, temp_x, temp_y])
                break
            possible_moves.append([start_x, start_y, temp_x, temp_y])
            
    # check for king
    if block.is_king():
        # check up
        if start_y - 1 >= 0:
            if board[start_y-1][start_x].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x, start_y-1])
                
            # check up right
            if start_x + 1 <= 7:
                if board[start_y-1][start_x+1].get_color() != block_color:
                    possible_moves.append([start_x, start_y, start_x+1, start_y-1])
                    
            # check up left
            if start_x - 1 >= 0:
                if board[start_y-1][start_x+1].get_color() != block_color:
                    possible_moves.append([start_x, start_y, start_x-1, start_y-1])
            
        # check down
        if start_y + 1 <= 7:
            if board[start_y+1][start_x].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x, start_y+1])
                
            # check down right
            if start_x + 1 <= 7:
                if board[start_y+1][start_x+1].get_color() != block_color:
                    possible_moves.append([start_x, start_y, start_x+1, start_y+1])
                    
            # check down left
            if start_x - 1 >= 0:
                if board[start_y+1][start_x-1].get_color() != block_color:
                    possible_moves.append([start_x, start_y, start_x-1, start_y+1])
        
        # check right
        if start_x + 1 <= 7:
            if board[start_y][start_x+1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x+1, start_y])
        
        # check left
        if start_x - 1 >= 0:
            if board[start_y][start_x-1].get_color() != block_color:
                possible_moves.append([start_x, start_y, start_x-1, start_y])
    
    return possible_moves


# obtain all possible next moves
def get_all_possible_moves(board, color):
    all_possible_moves = []
    for i in range(8):
        for k in range(8):
            if board[i][k].get_color() == color:
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
    new_board[start_y][start_x] = Block('.', 'none')
    
    return new_board
    
    
# calculates heuristic based on white and black score
def calculate_score(board):
    white_score = 0
    black_score = 0
    
    for i in range(8):
        for k in range(8):
            block = board[i][k]
            if block.get_color() == 'white':
                white_score += block.get_score()
            elif block.get_color() == 'black':
                black_score += block.get_score()

    return white_score - black_score     


# perform heuristic calculation at a depth of 3
def heuristic(board, depth, mode, a_cutoff, b_cutoff):
    
    # MAX node - initialize with -infinity
    if mode == 'MAX':
        best_score = -100000000000
        color = 'white'
        
    # MIN node - initialize with +infinity
    else:
        best_score = 100000000000
        color = 'black'
        
    all_possible_moves = get_all_possible_moves(board, color)
    best_move = all_possible_moves[0]
    
    for new_move in all_possible_moves:
    
        new_board = make_move(board, new_move)
        
        if mode == 'MAX':
            next_mode = 'MIN'
        else:
            next_mode = 'MAX'
        
        # base case
        if depth == 1:
            new_score = calculate_score(new_board)
        else:
            _, new_score = heuristic(new_board, depth - 1, next_mode, a_cutoff, b_cutoff)
        
        if mode == 'MAX':
            if new_score > best_score:
                best_score = new_score
                best_move = new_move
                a_cutoff = best_score
                
                # prune search tree
                if a_cutoff >= b_cutoff:
                    break
                
        else:
            if new_score < best_score:
                best_score = new_score
                best_move = new_move
                b_cutoff = best_score
                
                # prune search tree
                if b_cutoff <= a_cutoff:
                    break
                
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
    printed_board = [[0, 0, 1, 2, 3, 4, 5, 6, 7]]
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
        
    
    
