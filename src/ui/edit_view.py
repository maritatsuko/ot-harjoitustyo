from tkinter import ttk, constants, StringVar, Canvas, PhotoImage
from services.closet_service import closet_service


class EditView:
    """
    This class represents the view for editing an uploaded piece of clothing.
    """

    def __init__(self, root, piece, handle_edit_piece, handle_show_main_view):
        """Constructor for the EditView class.

        Args:
            root: Root window of the application.
            piece: The piece to be edited.
            handle_edit_piece: Function to handle editing a piece.
            handle_show_main_view: Function to show the main view.
            _frame: Frame for the view.
            _title_entry: Entry field for the title (name) of the piece.
            _color_entry: Combobox for selecting the color of the piece.
            _category_entry: Combobox for selecting the category of the piece.
            _image: PhotoImage object for displaying the selected image.
            _image_path: Path to the selected image.
            _image_area: Canvas for displaying the image.
            _error_variable: StringVar for error messages.
            _error_label: Label for displaying error messages.
        """

        self._root = root
        self._piece = piece
        self._handle_edit_piece = handle_edit_piece
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._old_title = piece.title
        self._title_entry = None
        self._colors = closet_service.get_all_colors()
        self._color_entry = None
        self._categories = closet_service.get_all_categories()
        self._category_entry = None
        self._image = None
        self._image_path = None
        self._image_area = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Pack the frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the frame."""
        self._frame.destroy()

    def _edit_handler(self):
        """Handle the editing process for a piece of clothing.
        """
        title = self._title_entry.get()
        color = self._color_entry.get()
        category = self._category_entry.get()
        image_path = self._image_path

        if len(title) == 0:
            self._show_error("Please enter a name for the piece")
            return
        if color not in self._colors:
            self._show_error("Please select a valid color")
            return
        if category not in self._categories:
            self._show_error("Please select a valid category")
            return

        try:
            closet_service.edit_piece(
                title, self._old_title, image_path, color, category)
            self._handle_edit_piece()
        except ValueError:
            self._show_error("Error while editing the piece")

    def _show_error(self, message):
        """Display an error message in the error label.

        Args:
            message: The error message to be displayed.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Hide the error label."""
        self._error_label.grid_remove()

    def _initialize_title_field(self):
        """Initialize the title field for the piece."""
        title_label = ttk.Label(master=self._frame, text="Name of the piece:")

        self._title_entry = ttk.Entry(master=self._frame)
        self._title_entry.insert(0, self._old_title)

        title_label.grid(row=1, column=0, sticky=constants.W)
        self._title_entry.grid(row=2, column=0, sticky=constants.EW)

    def _initialize_color_field(self):
        """Initialize the color field for the piece."""
        color_label = ttk.Label(master=self._frame, text="Color of the piece:")
        self._color_entry = ttk.Combobox(
            master=self._frame, values=self._colors, state="readonly")
        self._color_entry.set(self._piece.color)

        color_label.grid(row=3, column=0, sticky=constants.W)
        self._color_entry.grid(row=4, column=0, sticky=constants.EW)

    def _initialize_category_field(self):
        """Initialize the category field for the piece."""
        category_label = ttk.Label(
            master=self._frame, text="Category of the piece:")
        self._category_entry = ttk.Combobox(
            master=self._frame, values=self._categories, state="readonly")
        self._category_entry.set(self._piece.category)

        category_label.grid(row=5, column=0, sticky=constants.W)
        self._category_entry.grid(row=6, column=0, sticky=constants.EW)

    def _show_image(self):
        """Show the image selection dialog and display the selected image."""
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
        """Initialize the picture field for the piece."""
        self._image_area = Canvas(
            self._frame, width=800, height=800, bg="white")
        self._image_area.grid(row=7, column=0, padx=5,
                              pady=5, sticky=constants.EW)
        # Display the existing image if available
        if self._piece.image_path:
            self._image_path = self._piece.image_path
            self._image = PhotoImage(file=self._image_path)
            self._image_area.create_image(0, 0, image=self._image, anchor="nw")
            self._image_area.image = self._image
        # copilot generated code ends here

    def _initialize(self):
        """Initialize the EditView."""
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)

        label = ttk.Label(master=self._frame, text="Edit the piece here!")

        image_button = ttk.Button(
            master=self._frame, text="Select image (.png, max size 800x800)", command=self._show_image)
        save_button = ttk.Button(
            master=self._frame, text="Save edits", command=self._edit_handler)
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
        save_button.grid(row=8, column=1, padx=5, pady=5, sticky=constants.E)

        self._hide_error()
