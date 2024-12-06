import tkinter as tk

class Game(tk.Tk):
  def set_up_playground(self):
    self.clear_content()
    self.back_button = tk.Button(self, text="<", font='Arial, 25', command= self.set_up_title_screen)
    self.back_button.grid(row = 0, column = 0)


  def clear_content(self):
    for widget in self.winfo_children():
      widget.destroy()

  def set_up_title_screen(self):
    self.clear_content()
    self.title_screen_img = tk.PhotoImage(file='tic-tac-toe-2/assets/title_screen.png')
    self.title_screen_img = self.title_screen_img.subsample(2,2)
    tk.Label(self, image=self.title_screen_img).grid(row=0, column=0)

    self.play_button = tk.Button(self, text="Play", font='Arial, 20', borderwidth= 0  , width= 8, height=2, command=self.set_up_playground)
    self.play_button.place(x=350, y=300)


  def __init__(self):
    super().__init__()
    self.title("Tic-Tac-Toe 2")
    self.geometry("800x400")
    self.resizable(False, False)

    self.set_up_title_screen()


    


def main():
  Game().mainloop()

if __name__ == "__main__":
  main()