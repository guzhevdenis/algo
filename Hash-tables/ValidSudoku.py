# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the
# digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not
# necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku_old(board):
        #check in rows
        for i in range(9):
            sudoku_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(9):
                if (board[i][j] in sudoku_list):
                    sudoku_list.remove(board[i][j])

                elif(board[i][j] == "."):
                    continue
                else: 
                    return False 
        #check in columns 
        for i in range(9):
            sudoku_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(9):
                if (board[j][i] in sudoku_list):
                    sudoku_list.remove(board[j][i])
                elif(board[j][i] == "."):
                    continue
                else: 
                    return False 
        #check in cells

        cells = [0,3,6]
        for k in cells:
            for p in cells:
                sudoku_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                for i in range(3): 
                    for j in range(3):
                        if (board[j+k][i+p] in sudoku_list):
                            sudoku_list.remove(board[j+k][i+p])
                        elif(board[j+k][i+p] == "."):
                            continue
                        else: 
                            return False
        return True

def isValidSudoku (board):
# Create tracking structures for rows, columns, and 3x3 sub-boxes.
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Iterate over each cell in the 9x9 board.
        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                # Skip checking if the cell is empty.
                if cell_value == '.':
                    continue
              
                # Convert str digit to int and adjust index to zero-based.
                num = int(cell_value) - 1
              
                # Calculate box index for 3x3 sub-boxes using integer division.
                box_index = (i // 3) * 3 + j // 3
              
                # If the number has already been encountered in current
                # row, column or box, sudoku condition is violated.
                if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                    return False
              
                # Mark current num as encountered in current row, column and box.
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_index][num] = True

        # If no conditions are violated, then the board is a valid sudoku.
        return True
