from datastruct.ImageLabel import ImageLabel
from datastruct.SwtImage import SwtImage
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy


class ImageProcessor:
    def __init__(self):
        self.raw_image = None
        self.array_image = None
        self.bw_image = None
        self.canny_image = None
        self.trimmed_image = None

    def open_image(self, image:Image):
        self.raw_image = image
        self.array_image = numpy.array(self.raw_image)

    def process_edge(self):
        self.bw_image = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2GRAY)
        self.canny_image = cv2.Canny(self.bw_image, 50, 100)

    def trim_background(self):
        self.
