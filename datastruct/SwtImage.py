import cv2
import numpy


class SwtImage:
    image_rgb = None
    image_gray = None
    image_canny = None
    image_thin = None

    def open_image(self, image_path):
        """opens an image from a path, convert it to an array of rgb values, then returns itself as object"""
        self.image_rgb = cv2.imread(str(image_path))
        return self

    def convert_gray(self, forced=False):
        """converts the image into grayscale"""
        if (self.image_gray is None) or forced:
            self.image_gray = cv2.cvtColor(self.image_rgb, cv2.COLOR_BGR2GRAY)
            return self.image_gray
        else:
            return self.image_gray

    def get_stroke(self, forced=False):
        """highlight the strokes in the image"""
        if (self.image_canny is None) or forced:
            try:
                self.image_canny = cv2.Canny(self.image_gray, 50, 100)
            except:
                print("gray image is not set")


    def thinning(self, forced=False):
        """this function applies the erosion structure into the image.
        erosion structure is replacing each pixel in the center with the minimum of the overlap.
        """
        erosion_structure = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        self.image_thin = cv2.erode(self.image_canny, erosion_structure)
