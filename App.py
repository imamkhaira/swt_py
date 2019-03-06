from tkinter import *
from screen.Home import Home
from Debug import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.content = Home(self)
        self.content.grid(row=1, column=1)
        self.previous = []
        self.title("Stroke-Width Transform")
        log("program started")

    def switch_frame(self, new_frame:Frame):
        self.content.destroy()
        self.previous.append(self.content)
        self.content = new_frame
        self.content.grid(row=1, column=1)
        log("frame switch success")

    def back_frame(self):
        self.content.destroy()
        #new_frame = self.previous.pop()
        #self.content = new_frame
        #self.content.grid(row=1, column=1)
        log("frame switch success")


if __name__ == "__main__":
    app = App()
    app.mainloop()



