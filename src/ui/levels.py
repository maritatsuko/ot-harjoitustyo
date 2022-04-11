from tkinter import Tk, ttk, constants
#from loginscreen import LoginUI

class LevelsUI:
    def __init__(self, root):
        self._root = root
    
    def start(self):
        heading_label = ttk.Label(master=self._root, background="white", text="Choose level:")
        self.logout = ttk.Button(master=self._root, text="Log out", command=self._logging_out)
        self.level1 = ttk.Button(master=self._root, text="Level 1", command=self._level_click)
        self.level2 = ttk.Button(master=self._root, text="Level 2", command=self._level_click)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        self.logout.grid(row=0, column=0, columnspan=2, sticky=constants.E, padx=5, pady=5)
        self.level1.grid(row=3, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        self.level2.grid(row=4, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)     

    def _level_click(self):
       pass

    def _logging_out(self):
        pass

window = Tk()
window.title("Mochi - Levels")
window.configure(bg="pink")

ui = LevelsUI(window)
ui.start()
window.mainloop()