import tkinter as tk
from tkinter import messagebox

# Sudoku Solver using Backtracking
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False
    return True

def validate_input(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0  # Temporarily clear the cell
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num  # Restore the cell
    return True

# GUI for Sudoku Input and Display
def create_grid():
    for i in range(9):
        for j in range(9):
            cell = tk.Entry(grid_frame, width=2, font=('Arial', 18), justify='center', bg='white')
            cell.grid(row=i, column=j, padx=5, pady=5)
            cells[(i, j)] = cell

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = cells[(i, j)].get()
            if value.isdigit():
                num = int(value)
                if num < 1 or num > 9:
                    messagebox.showerror("Error", f"Invalid number at row {i+1}, column {j+1}. Enter numbers between 1 and 9.")
                    return None
                row.append(num)
            elif value == "":
                row.append(0)
            else:
                messagebox.showerror("Error", f"Invalid input at row {i+1}, column {j+1}. Enter only numbers or leave blank.")
                return None
        board.append(row)
    return board

def display_board(board):
    for i in range(9):
        for j in range(9):
            cells[(i, j)].delete(0, tk.END)
            if board[i][j] != 0:
                cells[(i, j)].insert(0, board[i][j])

def solve_puzzle():
    board = get_board()
    if board is None:
        return

    if not validate_input(board):
        messagebox.showerror("Error", "Invalid Sudoku puzzle. Check the input for conflicts.")
        return

    if solve_sudoku(board):
        display_board(board)
        messagebox.showinfo("Success", "Sudoku Solved Successfully!")
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            cells[(i, j)].delete(0, tk.END)

# Initialize GUI
root = tk.Tk()
root.title("Sudoku Solver")

cells = {}

# Create a frame for the grid
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

create_grid()

# Buttons for Solve and Clear
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

solve_button = tk.Button(button_frame, text="Solve", command=solve_puzzle, bg='lightgreen', font=('Arial', 14))
solve_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_grid, bg='lightcoral', font=('Arial', 14))
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()

