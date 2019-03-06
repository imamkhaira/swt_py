from tkinter import Frame, SUNKEN, Button
from datastruct.ImageLabel import ImageLabel
from PIL import Image, ImageTk
import cv2
from Debug import log


class LearnController:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.image_open= Image.open("etc/open.PNG")
        self.image_close
        log("launching learn hai gamghe")

    def open(self):
        self.parent_window.back_frame()


class Learn(Frame, LearnController):
    def __init__(self, parent_window):
        LearnController.__init__(self, parent_window)
        Frame.__init__(self, self.parent_window)

        # creates the (l)eft, (r)ight and (b)ottom pane
        l_pane = Frame(self, relief=SUNKEN, height=2, bd=1)
        button_open = Button(l_pane, text="Open...", command=self.open)
        image_open = ImageLabel(l_pane, self.image_open).grid()

        r_pane = Frame(self, relief=SUNKEN, height=2, bd=1)
        button_save = Button(r_pane, text="Save Data")

        b_pane = Frame(self, relief=SUNKEN, height=2, bd=1)

        l_pane.grid(row=0, column=0)
        r_pane.grid(row=0, column=1)
        b_pane.grid(row=1, column=0, columnspan=2)




