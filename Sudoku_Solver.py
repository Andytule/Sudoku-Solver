board_1 = [
    [3,0,0,0,2,9,0,0,4],
    [0,0,0,5,7,8,0,3,2],
    [0,0,2,0,0,0,0,0,0],
    [0,7,0,0,5,0,0,0,1],
    [1,9,4,8,0,0,0,2,0],
    [2,0,0,9,0,0,6,0,0],
    [7,0,0,0,8,5,2,0,9],
    [4,0,9,0,1,6,8,0,7],
    [5,0,0,0,0,2,3,0,6]
]

#Solves the board
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

# Determines if the number for the square(0) is valid in that position according
#   to the rules of Sudoku
def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range((box_y * 3), ((box_y * 3) + 3)):
        for j in range((box_x * 3), ((box_x * 3) + 3)):
            if (board[i][j] == num) and ((i, j) != pos):
                return False
    return True

# Print and updated version of the current board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Find the next empty square (0) in the Sudoku grid
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return (i, j)
    return None

print_board(board_1)
solve(board_1)
print("=====================")
print_board(board_1)