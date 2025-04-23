from tkinter import ttk, constants, StringVar, Canvas, PhotoImage
from services.closet_service import closet_service


class UploadView:

    def __init__(self, root, handle_upload_piece, handle_show_main_view):

        self._root = root
        self._handle_upload_piece = handle_upload_piece
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._title_entry = None
        self._colors = ["red", "blue", "green", "yellow", "brown",
                        "black", "white", "grey", "purple", "pink", "multi"]
        self._color_entry = None
        self._categories = ["top", "t-shirt", "sweater", "hoodie",
                       "jacket", "dress", "skirt", "pants", "shorts"]
        self._category_entry = None
        self._image = None
        self._image_path = None
        self._image_area = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _upload_handler(self):
        title = self._title_entry.get()
        color = self._color_entry.get()
        category = self._category_entry.get()
        image_path = self._image_path

        if len(title) == 0:
            self._show_error("Please enter a name for the piece")
            return
        if color == "Select color" or color not in self._colors:
            self._show_error("Please select a valid color")
            return
        if category == "Select category" or category not in self._categories:
            self._show_error("Please select a valid category")
            return

        try:
            closet_service.upload_piece(title, image_path, color, category)
            self._handle_upload_piece()
        except ValueError:
            self._show_error(
                f"A piece with the name {title} has already been uploaded")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_title_field(self):
        title_label = ttk.Label(master=self._frame, text="Name of the piece:")

        self._title_entry = ttk.Entry(master=self._frame)

        title_label.grid(row=1, column=0, sticky=constants.W)
        self._title_entry.grid(row=2, column=0, sticky=constants.EW)

    def _initialize_color_field(self):
        color_label = ttk.Label(master=self._frame, text="Color of the piece:")
        self._color_entry = ttk.Combobox(
            master=self._frame, values=self._colors, state="readonly")
        self._color_entry.set("Select color")

        color_label.grid(row=3, column=0, sticky=constants.W)
        self._color_entry.grid(row=4, column=0, sticky=constants.EW)
    
    def _initialize_category_field(self):
        category_label = ttk.Label(master=self._frame, text="Category of the piece:")
        self._category_entry = ttk.Combobox(
            master=self._frame, values=self._categories, state="readonly")
        self._category_entry.set("Select category")

        category_label.grid(row=5, column=0, sticky=constants.W)
        self._category_entry.grid(row=6, column=0, sticky=constants.EW)

    def _show_image(self):
        self._image_path = closet_service.show_image()
        if not self._image_path:
            self._show_error("Please select an image")
            return
        self._hide_error()
        self._image = PhotoImage(file=self._image_path)

        # copilot generated code starts here
        self._image_area.create_image(0, 0, image=self._image, anchor="nw")
        self._image_area.image = self._image

    def _initialize_picture_field(self):
        self._image_area = Canvas(
            self._frame, width=800, height=800, bg="white")
        self._image_area.grid(row=7, column=0, padx=5,
                              pady=5, sticky=constants.EW)
        # copilot generated code ends here

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)

        label = ttk.Label(master=self._frame, text="Upload a new piece here!")

        image_button = ttk.Button(
            master=self._frame, text="Select image (.png, max size 800x800)", command=self._show_image)
        upload_button = ttk.Button(
            master=self._frame, text="Upload piece", command=self._upload_handler)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_show_main_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(row=0, padx=5, pady=5, sticky=constants.EW)
        self._initialize_title_field()
        self._initialize_color_field()
        self._initialize_category_field()
        self._initialize_picture_field()
        image_button.grid(row=7, column=1, padx=5, pady=5, sticky=constants.E)
        cancel_button.grid(row=8, column=0, padx=5, pady=5, sticky=constants.W)
        upload_button.grid(row=8, column=1, padx=5, pady=5, sticky=constants.E)

        self._hide_error()
