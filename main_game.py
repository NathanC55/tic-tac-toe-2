import tkinter as tk
from tkinter import messagebox
class Tik_tac_toe(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Tic-Tac-Toe 2")
    self.geometry("800x400")
    self.resizable(False, False)

    self.current_player = "X"
    self.board = [["" for _ in range(3)] for _ in range(3)]
    self.buttons = [[None for _ in range(3)] for _ in range(3)]

    self.x_moves = []
    self.o_moves = []

    
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
    self.back_button = tk.Button(self, text="<", font='Arial, 25', command= self.confirm_back)
    self.back_button.grid(row = 0, column = 0)

    self.game_content = tk.Frame(self)
    self.game_content.grid(row=1, column=2, sticky="NSEW", padx=200, pady=50)
    self.create_board()
    self.reset_board()
  
  def confirm_back(self):
    # Show confirmation dialog
    answer = messagebox.askyesno("Confirm", "Are you sure you want to leave?")
    if answer:  # If user clicks "Yes"
        self.set_up_title_screen()

  def create_board(self):
    for row in range(3):
      for col in range(3):
        button = tk.Button(self.game_content,text="",font=("Arial", 24),width=5,height=2, command=lambda r=row, c=col: self.make_move(r, c))
        button.grid(row=row, column=col)
        self.buttons[row][col] = button

  def make_move(self, row, col):
    if self.board[row][col] == "":

      if self.current_player == 'X':
        if len(self.x_moves) == 3:
          # Get the first move from the list
          old_move = self.x_moves[0]
          
          # Clear the corresponding button and board position
          self.buttons[old_move[0]][old_move[1]].config(text="", state="normal",command=lambda r=old_move[0], c=old_move[1]: self.make_move(r, c))
          self.board[old_move[0]][old_move[1]] = ""
          

          # Remove the first move from the list
          self.x_moves.pop(0)
          
          # Add the new move to the list
        self.x_moves.append((row, col))
          
        # Shows the next move to disappear
        if len(self.x_moves) == 3:
          next_move_to_disappear = self.x_moves[0]
          self.buttons[next_move_to_disappear[0]][next_move_to_disappear[1]].config(fg = 'yellow')




      elif self.current_player == 'O':
        if len(self.o_moves) == 3:
          # Get the first move from the list
          old_move = self.o_moves[0]

          # Clear the corresponding button and board position
          self.buttons[old_move[0]][old_move[1]].config(text="", state="normal", command=lambda r=old_move[0], c=old_move[1]: self.make_move(r, c))
          self.board[old_move[0]][old_move[1]] = ""

          # Remove the first move from the list
          self.o_moves.pop(0)

        # Add the new move to the list
        self.o_moves.append((row, col))

        # Shows the next move to disappear
        if len(self.o_moves) == 3:
          next_move_to_disappear = self.o_moves[0]
          self.buttons[next_move_to_disappear[0]][next_move_to_disappear[1]].config(fg = 'yellow')



    self.board[row][col] = self.current_player
    self.buttons[row][col].config(text=self.current_player, fg="blue" if self.current_player == 'X' else "red", command = lambda : None)

    if self.check_winner():
      messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
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

    
def main():
  Tik_tac_toe().mainloop()

if __name__ == "__main__":
  main()
