from tkinter import Frame, Label, Button, SUNKEN, PhotoImage, Text
from datastruct.ImageLabel import ImageLabel
from datastruct.ImageProcessor import ImageProcessor
from PIL import Image


class RecognitionController:
    def __init__(self, parent_window)
        self.parent_window      = parent_window    # of type Tk
        self.image_processor    = ImageProcessor()
        self.text_output        = None # of type Text, to display output
        self.image_open         = Image.open("etc/example.png") # set the default input image
        self.image_cc           = None
        self.imagelabel_open    = None
        self.imagelabel_cc      = None

    def process_img(self, input_img):
        self.




class Recognition(Frame, RecognitionController):
    def __init__(self, parent_window):
        self.parent_window = parent_window
        Frame.__init__(self, self.parent_window, height=2, bd=1, relief=SUNKEN)
        
        # 
        label_recognition 	= Label(self, text="Recognition")
        self.imagelabel_open= ImageLabel(self, self.image_open)
        button_open         = Button(self, text="Open...")
        button_back         = Button(self, text="Back")
        label_cc            = Label(self, text="1. Chain Code result")
        self.imagelabel_cc  = ImageLabel
        