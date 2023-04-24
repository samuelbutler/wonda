import random


def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))


def next_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return -1, -1


def is_valid(grid, num, row, col):
    if num in grid[row]:  # Check row
        return False
    if num in (grid[i][col] for i in range(9)):  # Check column
        return False
    
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:  # Check 3x3 box
                return False
    return True


def sudoku_solver(grid):
    row, col = next_empty(grid)
    if row == -1:  # No more empty cells, solution found
        return True
    
    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num
            if sudoku_solver(grid):  # Recursion
                return True
            grid[row][col] = 0  # Backtracking
    return False


def sudoku_generator():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(20):  # Fill grid with random numbers
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(grid, num, row, col):
            grid[row][col] = num

    if sudoku_solver(grid):  # Solve the randomly filled grid
        return grid
    return sudoku_generator()  # If unsolvable, generate a new one


sudoku_puzzle = sudoku_generator()
print_grid(sudoku_puzzle)