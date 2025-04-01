from tkinter import ttk, constants

class MainView:
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
        label = ttk.Label(master=self._frame, text="Welcome to ClosetApp!")

        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._handle_show_start_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(padx=5, pady=5, sticky=constants.EW)
        logout_button.grid(row=1, column=1, padx=5, pady=5, sticky=constants.E)