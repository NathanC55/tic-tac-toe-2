import tkinter as tk


class Game(tk.Tk):

  def __init__(self):
    super().__init__()
    self.title("Tic-Tac-Toe 2")




def main():
  Game().mainloop()

if __name__ == "__main__":
  main()