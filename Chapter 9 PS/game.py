import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")
root.resizable(False, False)

# Initialize variables
current_player = "X"
board = [""] * 9

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None

# Function for button click
def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not check_winner():
        buttons[index]["text"] = current_player
        board[index] = current_player
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="")

# Create buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
