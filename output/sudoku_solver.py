def is_valid(grid, row, col, num):
    # Check if the number is in the row or column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check if the number is in the 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def sudoku_solver(grid):
    # Find an empty cell
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    row, col = empty_cell

    # Attempt to fill the cell with a valid number
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            # Continue with the next cell
            if sudoku_solver(grid):
                return True

            # If the placement was wrong, reset the cell to 0
            grid[row][col] = 0

    return False


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


# Example usage
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if sudoku_solver(sudoku_puzzle):
    for row in sudoku_puzzle:
        print(row)
else:
    print("No solution exists.")

# Read the generated Sudoku puzzle from the input file
import json
with open('sudoku_puzzle.json', 'r') as file:
    sudoku_puzzle = json.load(file)['data']

# Solve the generated Sudoku puzzle using the solver
if sudoku_solver(sudoku_puzzle):
    for row in sudoku_puzzle:
        print(row)
else:
    print('No solution exists.')