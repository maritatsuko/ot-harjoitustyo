from tkinter import Tk, ttk, constants

class LevelsUI:
    def __init__(self, root, logging_out):
        self._root = root
        self._logging_out = logging_out
        self._frame = None

        self.start()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def start(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, background="white", text="Choose level:")
        self.logout = ttk.Button(master=self._frame, text="Log out", command=self._logging_out)
        self.level1 = ttk.Button(master=self._frame, text="Level 1", command=self._level_click)
        self.level2 = ttk.Button(master=self._frame, text="Level 2", command=self._level_click)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        self.logout.grid(row=0, column=0, columnspan=2, sticky=constants.E, padx=5, pady=5)
        self.level1.grid(row=3, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        self.level2.grid(row=4, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)     

    def _level_click(self):
       pass


#window = Tk()
#window.title("Mochi - Levels")

#ui = LevelsUI(window)
#ui.start()
#window.mainloop()