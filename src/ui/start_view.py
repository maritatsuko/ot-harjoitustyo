from tkinter import ttk, constants, StringVar
from services.closet_service import closet_service

class StartView:

    def __init__(self, root, handle_login, handle_show_create_acc_view):

        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_acc_view = handle_show_create_acc_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
    
        try:
            closet_service.login(username, password)
            self._handle_login()
        except Exception:
            self._show_error("Invalid username or password")
        
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()
    
    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username:")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0, sticky=constants.W)
        self._username_entry.grid(row=2, column=0, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password:")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(row=3, column=0, sticky=constants.W)
        self._password_entry.grid(row=4, column=0, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)

        label = ttk.Label(master=self._frame, text="Hello world!")

        login_button = ttk.Button(master=self._frame, text="Login", command=self._login_handler)
        create_acc_button = ttk.Button(master=self._frame, text="Create New Account", command=self._handle_show_create_acc_view)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(row=0, padx=5, pady=5, sticky=constants.EW)
        self._initialize_username_field()
        self._initialize_password_field()

        create_acc_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.E)
        login_button.grid(row=5, column=1, padx=5, pady=5, sticky=constants.E)

        self._hide_error()