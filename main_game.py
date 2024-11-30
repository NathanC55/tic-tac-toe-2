import tkinter as tk


class Game(tk.Tk):

  def __init__(self):
    super().__init__()
    self.title("Tic-Tac-Toe 2")

    self.title_screen_img = tk.PhotoImage(file='tic-tac-toe-2/assets/title_screen.png')
    self.title_screen_img = self.title_screen_img.subsample(2,2)
    tk.Label(self, image=self.title_screen_img).grid(row=0, column=0)


def main():
  Game().mainloop()

if __name__ == "__main__":
  main()