from tkinter import Frame, PhotoImage, Label, Button, E, W, N
from screen.Learn import Learn


class HomeController:
    parent_window = None

    def open_learn(self):
        self.parent_window.switch_content(Learn(self.parent_window))
        print("clicked the recognition button")


class Home(Frame, HomeController):
    def __init__(self, parent_window):
        self.parent_window = parent_window
        Frame.__init__(self, self.parent_window)

        # create the logo object
        swt_logo_png = PhotoImage(file="etc/logo.png")
        swt_logo = Label(self, image=swt_logo_png)
        swt_logo.photo = swt_logo_png

        # create an array containing all button object. easier to manage wkwk
        b_recognition = Button(self, text="Character Recognition")
        b_learning = Button(self, text="Character Learning", command=self.open_learn)
        b_database = Button(self, text="Database")
        b_manual = Button(self, text="Manual")
        b_about = Button(self, text="About SWT")
        b_exit = Button(self, text="Exit", command=lambda: exit(0))

        # set the set padding
        set_padx = 10
        set_pady = 5

        # display the logo first into the grid
        swt_logo.grid(column=0, row=0, columnspan=2, sticky=N, padx=65, pady=40)

        # then display the buttons into the grid.
        b_recognition.grid(column=0, row=1, sticky=(E, W), padx=set_padx, pady=set_pady)
        b_learning.grid(column=1, row=1, sticky=(E, W), padx=set_padx)
        b_database.grid(column=0, row=2, sticky=(E, W), padx=set_padx, pady=set_pady)
        b_manual.grid(column=1, row=2, sticky=(E, W), padx=set_padx)
        b_about.grid(column=0, row=3, sticky=(E, W), padx=set_padx, pady=set_pady)
        b_exit.grid(column=1, row=3, sticky=(E, W), padx=set_padx)
