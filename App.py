from tkinter import *
from screen.Home import Home
from Debug import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.content = Home(self)
        self.content.grid()
        self.previous_content = []
        self.title("Stroke-Width Transform")
        log("program started")

    def switch_frame(self, new_frame:Frame):
        self.content.grid_forget()
        self.previous_content.append(self.content)
        self.content = new_frame
        self.content.grid()
        log("frame switch success")


if __name__ == "__main__":
    app = App()
    app.mainloop()



