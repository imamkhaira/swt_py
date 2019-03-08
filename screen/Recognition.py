from tkinter import Frame, Label, Button, SUNKEN, PhotoImage


class RecognitionController:
    parent_window = None    # of type Tk


class Recognition(Frame, RecognitionController):
    def __init__(self, parent_window):
        self.parent_window = parent_window
        Frame.__init__(self, self.parent_window)
        self.top_frame = Frame(self, height=2, bd=1, relief=SUNKEN)
        self.bot_frame = Frame(self, height=2, bd=1, relief=SUNKEN)

        label_rec 		= Label(self.top_frame, text="Recognition")
        self.image_path = "etc/logo.png"
        self.open_img 	= PhotoImage(file=self.image_path).subsample(1,1)
        label_open_img 	= Label(self.top_frame, image=self.open_img)
        label_open_img.photo = self.open_img

        button_open = Button(self, text="Open...")

        label_thinning 	= Label(self.bot_frame, text="1. Thinning")
        label_segment 	= Label(self.bot_frame, text="2. segmentation")