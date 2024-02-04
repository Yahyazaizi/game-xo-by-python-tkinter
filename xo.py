import tkinter as tk
from tkinter import messagebox
import random



def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col].config(text=players1[current_player], state='disabled')
        board[row][col] = players[current_player]

def on_click(row, col):
    global current_player

    if board[row][col] == ' ':
        buttons[row][col].config(text=players[current_player], state='disabled')
        board[row][col] = players1[current_player]
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            root.quit()
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            messagebox.showinfo("Tie", "It's a tie!")
            root.quit()
        else:
            current_player = (current_player+1) % 2
            computer_move()  
    else:
        messagebox.showwarning("Invalid Move", "That cell is already taken. Try again.")

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X','X']
players1 = [ 'O','O']

current_player =0

buttons = [[0, 0, 0] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 30), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
