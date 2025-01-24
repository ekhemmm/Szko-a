import tkinter as tk
from tkinter import messagebox
from functools import partial

class TicTacToe:
    def __init__(self, root):
        self.board = [""] * 9
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("450x450")
        self.current_player = "X"
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                button = tk.Button(self.root, text="", width=20, height=8, command=partial(self.on_button_click, index))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

def main():
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()