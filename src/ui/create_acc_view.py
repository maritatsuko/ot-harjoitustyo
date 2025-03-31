from tkinter import ttk, constants

class CreateAccView:

    def __init__(self, root, handle_show_start_view):

        self._root = root
        self._handle_show_start_view = handle_show_start_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Create a new account here!")
        username_label = ttk.Label(master=self._frame, text="Username:")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password:")
        password_entry = ttk.Entry(master=self._frame)
        create_acc_button = ttk.Button(master=self._frame, text="Create Account")
        login_button = ttk.Button(master=self._frame, text="Login instead", command=self._handle_show_start_view)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(padx=5, pady=5, sticky=constants.EW)
        username_label.grid(row=1, column=0, sticky=constants.W)
        username_entry.grid(row=2, column=0, sticky=constants.EW)
        password_label.grid(row=3, column=0, sticky=constants.W)
        password_entry.grid(row=4, column=0, sticky=constants.EW)
        login_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.E)
        create_acc_button.grid(row=5, column=1, padx=5, pady=5, sticky=constants.E)