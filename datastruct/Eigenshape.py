import pytesseract as Ocr
from PIL import Image, ImageTk
import cv2
import numpy
Ocr.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

class EigenShape:
    def __init__(self, image_PIL):
        self.raw_image = image_PIL
        self.array_img = None
        self.bw_img = None
        self.processed_img = None
        gaussian_filter = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        treshold_filter = cv2.THRESH_BINARY

        self.array_img = numpy.asarray(self.raw_image)
        self.bw_img = cv2.cvtColor(self.array_img, cv2.COLOR_BGR2GRAY)

        # Applies kernel dilation filter followed by erosion filter
        kernel = numpy.ones((1, 1), numpy.uint8)
        self.processed_img = cv2.dilate(self.bw_img, kernel, iterations=1)
        self.processed_img = cv2.erode(self.processed_img, kernel, iterations=1)

        # apply adaptive tresholding to convert it to binary color (black and white only, no gray)
        self.processed_img = cv2.adaptiveThreshold(self.processed_img, 255, gaussian_filter, treshold_filter, 31, 2)

    def get_processed_image(self):
        return self.processed_img

    def get_detected_text(self):
        return Ocr.image_to_string(self.processed_img)
