import tkinter as tk
from tkinter import messagebox
class Game(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Tic-Tac-Toe 2")
    self.geometry("800x400")
    self.resizable(False, False)

    self.current_player = "X"
    self.board = [["" for _ in range(3)] for _ in range(3)]
    self.buttons = [[None for _ in range(3)] for _ in range(3)]
    
    self.set_up_title_screen()

  def set_up_title_screen(self):
    self.clear_content()
    self.title_screen_img = tk.PhotoImage(file='tic-tac-toe-2/assets/title_screen.png')
    self.title_screen_img = self.title_screen_img.subsample(2,2)
    tk.Label(self, image=self.title_screen_img).grid(row=0, column=0)

    self.play_button = tk.Button(self, text="Play", font='Arial, 20', borderwidth= 0  , width= 8, height=2, command=self.set_up_playground)
    self.play_button.place(x=350, y=300)


  def set_up_playground(self):
    self.clear_content()
    self.back_button = tk.Button(self, text="<", font='Arial, 25', command= self.set_up_title_screen)
    self.back_button.grid(row = 0, column = 0)

    self.game_content = tk.Frame(self)
    self.game_content.grid(row=1, column=2, sticky="NSEW")
    self.create_board()

  def create_board(self):
    for row in range(3):
      for col in range(3):
        button = tk.Button(self.game_content,text="",font=("Arial", 24),width=5,height=2, command=lambda r=row, c=col: self.make_move(r, c))
        button.grid(row=row, column=col)
        self.buttons[row][col] = button


  def make_move(self, row, col):
    if self.board[row][col] == "":
      self.board[row][col] = self.current_player
      self.buttons[row][col].config(text=self.current_player, state="disabled")

    if self.check_winner():
      messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
      self.reset_board()

    elif all(all(cell != "" for cell in row) for row in self.board):
      messagebox.showinfo("Game Over", "It's a draw!")
      self.reset_board()

    else:
      self.current_player = "O" if self.current_player == "X" else "X"


  def check_winner(self):
    # Check rows and columns
    for i in range(3):
      if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ""
          or self.board[0][i] == self.board[1][i] == self.board[2][i] != ""
      ):
          return True
    # Check diagonals
    if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ""
        or self.board[0][2] == self.board[1][1] == self.board[2][0] != ""):
        return True
    
    return False
  def reset_board(self):
    self.board = [["" for _ in range(3)] for _ in range(3)]
    self.current_player = "X"
    for row in range(3):
      for col in range(3):
        self.buttons[row][col].config(text="", state="normal")

  def clear_content(self):
    for widget in self.winfo_children():
      widget.destroy()

  def clear_content(self):
    for widget in self.winfo_children():
      widget.destroy()

    
def main():
  Game().mainloop()

if __name__ == "__main__":
  main()



