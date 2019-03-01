from tkinter import Frame, Button, Label, PhotoImage, messagebox, filedialog
from tkinter import SUNKEN, E, W, TclError
import sys
import cv2
from PIL import Image, ImageTk


class LearnController:
    """Parameter: None
    this is the controller class of the character Learn screen. it has
    the controlled variable fields that consists of:
        - this one below is all input objects (e.g the one that will be modified)
        - in-process data field that holds the data during processing
        - output field that holds the finished data for output"""

    parent_window = None    # type: Tk
    frame_input = None     # type: Frame
    input_img = None        # type: Image
    label_input_img = None  # type:
    input_path = "etc/iium.png"

    thinned_img = None      # type: Image
    greyed_img = None       # type: Image
    edged_img = None        # type: Image
    
    frame_output = None     # type: Frame
    output_img = None       # type: PhotoImage
    output_path = "etc/iium.png"
    label_output_img = None # type:Label
    no_of_edges = 0         
    no_of_ends = 0
    char_label = ""

    def open_file(self):
        """Params: None
        To be activated when the "Open Image" button are clicked. it opens the file dialog, 
        and immediately render the selected image. an exception will be thrown if user 
        selected unsupported image. if exception occur, an error message will be
        displayed and the user can opt to repeat."""
        print("opened file selection dialog")
        try:
            self.input_path = filedialog.askopenfile().name
        except TclError:
            print("user selected unsupported image format")
            messagebox.showerror(title="Unsupported image", message="Only .PNG images are supported")
        except AttributeError:
            print("user clicked cancel")
            pass
    
    def analyze(self):
        self.input_path = "etc/logo.png"
        print("changed")
        self.input_img = ImageTk.PhotoImage(Image.open(self.input_path))
        self.label_input_img.configure(image=self.input_img)
        self.label_input_img.image = self.input_img

    


class Learn(Frame, LearnController):
    def __init__(self, parent_window):
        self.parent_window = parent_window
        Frame.__init__(self, self.parent_window)

        # the screen consists of three sub-frames. first is the input subframe,
        # next to it is the output subframe in the right, and the result frame
        # in the bottom side of the two first frames.
        # each frames are declared and followed by their respective widget.

        # input frame and its widgets
        self.frame_input = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_input, text="Input image").grid()
        self.input_img = ImageTk.PhotoImage(Image.open(self.input_path))
        self.label_input_img = Label(self.frame_input, image=self.input_img)
        self.label_input_img.grid()
        Button(self.frame_input, text="Open image..", command=self.open_file).grid()


        # output frame and its widgets
        self.frame_output = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_output, text="Output image").grid()
        self.output_img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(cv2.Canny(cv2.imread(self.output_path), 50,100), cv2.COLOR_BGR2RGB)))
        self.label_output_img = Label(self.frame_output, image=self.output_img)
        self.label_output_img.grid()
        Button(self.frame_output, text="Analyze", command=self.analyze).grid()

        # Result frame, and its widgets
        self.frame_result = Frame(self, height=2, bd=1, relief=SUNKEN)
        Label(self.frame_result, text="Result").grid()

        # grid the frames
        self.frame_input.grid(row=0, column=0)
        self.frame_output.grid(row=0, column=1)
        self.frame_result.grid(row=1, column=0, columnspan=2)
