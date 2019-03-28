from tkinter import *
from PIL import Image, ImageTk
from datastruct.ImageLabel import ImageLabel
from Debug import *
from screen.Learn import Learn
from screen.Recognition import Recognition
from datastruct.SwtImage import SwtImage
import cv2


class HomeController:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        log("loaded home controller")

    def exit(self):
        log("exiting..")
        exit(0)

    def launch_recognition(self):
        log("launching recognition")
        self.parent_window.switch_frame(Recognition(self.parent_window))


    def launch_learning(self):
        log("launching learning")
        self.parent_window.switch_frame(Learn(self.parent_window))


    def launch_database(self):
        log("launching database")


class Home(HomeController, Frame):
    def __init__(self, parent_window: Tk):
        HomeController.__init__(self, parent_window)
        Frame.__init__(self, self.parent_window)

        imagelabel_swtLogo = ImageLabel(self, Image.open("etc/logo.png"))
        button1 = Button(self, text="Character Learning", command=self.launch_learning)
        button2 = Button(self, text="Character Recognition", command=self.launch_recognition)
        button3 = Button(self, text="Shape Database", command=self.launch_database)
        button4 = Button(self, text="Exit Program", command=self.exit)

        padx, pady = 10, 5
        imagelabel_swtLogo.grid(row=0, column=0, columnspan=2, padx=padx, pady=pady, sticky=(E, W))
        button1.grid(row=1, column=0, sticky=(E, W), padx=padx, pady=pady)
        button2.grid(row=1, column=1, sticky=(E, W), padx=padx, pady=pady)
        button3.grid(row=2, column=0, sticky=(E, W), padx=padx, pady=pady)
        button4.grid(row=2, column=1, sticky=(E, W), padx=padx, pady=pady)
