from tkinter import *
from PIL import Image, ImageTk
import Debug
from cv2 import *


class ImageLabel(Label):
    def __init__(self, parent_window: Frame, image_pil):
        self.imagePIL = image_pil
        self.image = ImageTk.PhotoImage(self.imagePIL)
        Label.__init__(self, parent_window, image=self.image)
        Debug.log("displaying image")


    def change_image(self, new_image_pil):
        """ allows quick and simple image replacement by updating the image reference too."""
        self.imagePIL = new_image_pil
        self.image = ImageTk.PhotoImage(self.imagePIL)
        self.configure(image=self.image)
        Debug.log("image change occured")
