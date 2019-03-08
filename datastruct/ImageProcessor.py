from datastruct.ImageLabel import ImageLabel
from datastruct.SwtImage import SwtImage
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy


class ImageProcessor:
    def __init__(self, image:Image):
        self.raw_image = None
        self.array_image = None
        self.bw_image = None
        self.canny_image = None
        self.letters = None
        self.trimmed_image = []

        # take the raw image and convert it into array of pixels
        self.raw_image = image
        self.array_image = numpy.asarray(self.raw_image)

        # convert it into grayscale image and extract edges
        self.bw_image = cv2.cvtColor(self.array_image, cv2.COLOR_BGR2GRAY)
        self.canny_image = cv2.Canny(self.bw_image, 50, 100)

        # find contours of the image (the actual size of the font/text)
        self.letters = cv2.findContours(self.canny_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    def get_string_result(self):
        pil_images = []
        self.letters = sorted(self.letters, key=cv2.contourArea)

        # trim the image to remove excess background
        for letter in self.letters:
            x, y, w, h = cv2.boundingRect(letter)
            trimmed_letter = self.canny_image[y:y + h, x:x + w]
            self.trimmed_image.append(trimmed_letter)
            pil_images.append(Image.fromarray(trimmed_letter))

        return pil_images

    def get_letter_result(self):
        self.letters = sorted(self.letters, key=cv2.contourArea)[-1]
        x, y, w, h = cv2.boundingRect(self.letters)
        trimmed_letter = self.canny_image[y:y + h, x:x + w]

        return Image.fromarray(trimmed_letter)
