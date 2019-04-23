from tkinter import Frame, Label, Button, SUNKEN, PhotoImage, Text, E, W, filedialog, StringVar, Entry
from datastruct.ImageLabel import ImageLabel
from datastruct.ImageProcessor import ImageProcessor
from PIL import Image
from datastruct.Eigenshape import EigenShape


class RecognitionController:
    def __init__(self, parent_window):
        self.parent_window      = parent_window    # of type Tk
        self.image_open         = Image.open("etc/open2.png")  # set the default input image
        self.image_processor    = ImageProcessor(self.image_open)
        self.image_result       = self.image_processor.get_canny()
        self.imagelabel_open = None
        self.imagelabel_result = None
        self.text_recognition = None
        self.text_result = StringVar()  # of type Text/stringvar, to display output
        self.text_output_label = None

    def process_image(self, input_img):
        self.image_processor = ImageProcessor(input_img)
        self.text_recognition = EigenShape(input_img)
        #print(self.text_recognition.get_detected_text())
        return self.image_processor.get_canny(), self.text_recognition.get_detected_text()

    def open_file(self):
        image_filename = filedialog.askopenfilename(title="Select text image",
                                                    filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        try:
            print(image_filename)
            self.image_open = Image.open(image_filename)
            self.image_result, text = self.process_image(self.image_open)
            self.imagelabel_open.change_image(self.image_open)
            self.imagelabel_result.change_image(self.image_result)
            self.text_result.set(text)

        except AttributeError:
            #self.message = "user clicked cancel"
            print("user clicked cancel")
            pass


class Recognition(Frame, RecognitionController):
    def __init__(self, parent_window):
        RecognitionController.__init__(self, parent_window)
        Frame.__init__(self, self.parent_window, height=2, bd=1, relief=SUNKEN)

        open_button = Button(self, text="Open Image..", command=self.open_file)
        open_button.grid(padx=10, pady=5, sticky=(E, W))
        self.imagelabel_open = ImageLabel(self, self.image_open)
        self.imagelabel_open.grid(padx=10, pady=5, sticky=(E, W))

        self.imagelabel_result = ImageLabel(self, self.image_result)
        self.imagelabel_result.grid(padx=10, pady=5, sticky=(E, W))

        Label(self, text="OUTPUT:").grid()
        self.text_output_label = Label(self, textvariable=self.text_result)
        self.text_output_label.grid()


