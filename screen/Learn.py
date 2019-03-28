from tkinter import Frame, Label, Entry, SUNKEN, Button, filedialog, StringVar, W, E
from datastruct.ImageLabel import ImageLabel
from PIL import Image, ImageTk
from datastruct.ImageProcessor import ImageProcessor
import cv2
from Debug import log


class LearnController:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.imageProcessor = None
        self.input_img = Image.open("etc/open.png")
        self.output_img = self.process_image(self.input_img)
        self.imagelabel_output_img = None
        self.imagelabel_input_img = None
        self.letter_name = None
        self.message = StringVar("")
        self.name_entry = Entry
        self.data = dict()

        log("launching learn controller")

    def process_image(self, input_img):
        self.input_img = input_img
        self.imageProcessor = ImageProcessor(self.input_img)
        self.output_img = self.imageProcessor.get_letter_result()
        return self.output_img

    def open_file(self):
        image_filename = filedialog.askopenfilename(title="Select character image", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        try:
            self.message.set("opening "+image_filename)
            self.input_img = Image.open(image_filename)
            self.output_img = self.process_image(self.input_img)
            self.imagelabel_input_img.change_image(self.input_img)
            self.imagelabel_output_img.change_image(self.output_img)
            print("".join(self.imageProcessor.trimmed_image))
        except AttributeError:
            self.message = "user clicked cancel"
            pass

    def save_data(self):
        self.letter_name = self.name_entry.get()
        self.data[self.letter_name] = self.imageProcessor.trimmed_image
        self.message = "added "+self.letter_name
        log(self.message)

    def go_back(self):
        self.parent_window.back_frame()


class Learn(Frame, LearnController):
    def __init__(self, parent_window):
        LearnController.__init__(self, parent_window)
        Frame.__init__(self, self.parent_window)

        # the screen consists of three sub-frames. first is the input subframe,
        # next to it is the output subframe in the right, and the result frame
        # in the bottom side of the two first frames.
        # each frames are declared and followed by their respective widget.

        # input frame and its widgets
        self.frame_input = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_input, text="Input image").grid()

        self.imagelabel_input_img = ImageLabel(self.frame_input, self.input_img)
        self.imagelabel_input_img.grid()
        Button(self.frame_input, text="Open image..", command=self.open_file).grid()

        # output frame and its widgets
        self.frame_output = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_output, text="Output image").grid(row=0, column=0, columnspan=2)
        self.imagelabel_output_img = ImageLabel(self.frame_output, self.output_img)
        self.imagelabel_output_img.grid(row=1, column=0, columnspan=2)
        Label(self.frame_output, text="Letter name: ").grid(row=2, column=0, pady=15)
        self.name_entry = Entry(self.frame_output)
        self.name_entry.grid(row=2, column=1)
        Button(self.frame_output, text="Save Data", command=self.save_data).grid(row=3, column=0)
        Button(self.frame_output, text="Back", command=self.go_back).grid(row=3, column=1)

        # Result frame, and its widgets
        self.frame_result = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_result, text="Result").grid()
        Label(self.frame_result, text=self.message).grid(sticky=W+E)

        # grid the frames
        self.frame_input.grid(row=0, column=0)
        self.frame_output.grid(row=0, column=1)
        self.frame_result.grid(row=1, column=0, columnspan=2)




