from tkinter import ttk, constants, StringVar
from services.closet_service import closet_service

class UploadView:

    def __init__(self, root, handle_upload_piece, handle_show_main_view):

        self._root = root
        self._handle_upload_piece = handle_upload_piece
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._title_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _upload_handler(self):
        title = self._title_entry.get()

        if len(title) == 0:
            self._show_error("Please enter a name for the piece")
            return
        
        try:
            closet_service.upload_piece(title)
            self._handle_upload_piece()
        except ValueError:
            self._show_error(f"A piece with the name {title} has already been uploaded")
    
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

        upload_button = ttk.Button(master=self._frame, text="Upload piece", command=self._upload_handler)
        cancel_button = ttk.Button(master=self._frame, text="Cancel", command=self._handle_show_main_view)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(row=0, padx=5, pady=5, sticky=constants.EW)
        self._initialize_title_field()
        cancel_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.E)
        upload_button.grid(row=5, column=1, padx=5, pady=5, sticky=constants.E)

        self._hide_error()