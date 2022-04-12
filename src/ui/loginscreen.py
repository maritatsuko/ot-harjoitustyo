from tkinter import Tk, ttk, constants

class LoginUI:
    def __init__(self, root, logging_in):
        self._root = root
        self._logging_in = logging_in
        self.frame = None
        self.un_entry = None

        self.start()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def start(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, background="white", text="Hi! Welcome to Mochi, please log in:")
        username_label = ttk.Label(master=self._frame, background="white", text="Username: ")
        self.un_entry = ttk.Entry(master=self._frame)
        self.login = ttk.Button(master=self._frame, text="Log in", command=self._logging_in)
        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self.un_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.login.grid(row=3, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)     

    def logging_username(self):
        username = self.un_entry.get()
        return username
