from tkinter import ttk, constants, StringVar
from services.closet_service import closet_service

class CreateAccView:
    """
    This class represents the view for creating a new account.
    """

    def __init__(self, root, handle_create_acc, handle_show_start_view):
        """Contructor for the CreateAccView class.

        Args:
            root: Root window of the application.
            handle_create_acc: Function to handle account creation.
            handle_show_start_view: Function to show the start view.
            _frame: Frame for the view.
            _username_entry: Entry field for username.
            _password_entry: Entry field for password.
            _error_variable: StringVar for error messages.
            _error_label: Label for displaying error messages.
        """

        self._root = root
        self._handle_create_acc = handle_create_acc
        self._handle_show_start_view = handle_show_start_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Pack the frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the frame."""
        self._frame.destroy()
    
    def _create_acc_handler(self):
        """Handle the account creation process.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Please enter username and password")
            return
        
        try:
            closet_service.create_user(username, password)
            self._handle_create_acc()
        except ValueError:
            self._show_error(f"Username {username} already exists")
    
    def _show_error(self, message):
        """Display an error message in the error label.

        Args:
            message: The error message to display.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Hide the error label."""
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Initialize the username field in the frame."""
        username_label = ttk.Label(master=self._frame, text="Username:")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=2, column=0, sticky=constants.W)
        self._username_entry.grid(row=3, column=0, sticky=constants.EW)

    def _initialize_password_field(self):
        """Initialize the password field in the frame."""
        password_label = ttk.Label(master=self._frame, text="Password:")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(row=4, column=0, sticky=constants.W)
        self._password_entry.grid(row=5, column=0, sticky=constants.EW)

    def _initialize(self):
        """Initialize the CreateAccView."""
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(row=0, column=0, padx=5, pady=5)

        label = ttk.Label(master=self._frame, text="Create a new account here!")

        create_acc_button = ttk.Button(master=self._frame, text="Create Account", command=self._create_acc_handler)
        login_button = ttk.Button(master=self._frame, text="Login instead", command=self._handle_show_start_view)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(row=1, padx=5, pady=5, sticky=constants.EW)
        self._initialize_username_field()
        self._initialize_password_field()
        login_button.grid(row=6, column=0, padx=5, pady=5, sticky=constants.E)
        create_acc_button.grid(row=6, column=1, padx=5, pady=5, sticky=constants.E)

        self._hide_error()