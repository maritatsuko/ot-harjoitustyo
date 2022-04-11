from tkinter import Tk
from loginscreen import LoginUI
from levels import LevelsUI

class UserInterface:
    def __init__(self, root):
        self._root = root
        self._current = None
    
    def start(self):
        self._open_loginscreen()
    
    def _hide_current_screen(self):
        if self._current:
            self._current.destroy()
        
        self._current = None
    
    def _logging_in(self):
        #username = self._un_entry.get()
        self._open_levels()
    
    def _logging_out(self):
        self._open_loginscreen()
    
    def _open_loginscreen(self):
        self._hide_current_screen()
        
        self._current = LoginUI(self._root, self._logging_in)
        
        self._current.pack()
    
    def _open_levels(self):
        self._hide_current_screen()

        self._current = LevelsUI(self._root, self._logging_out)
        
        self._current.pack()

window = Tk()
window.title("Mochi")
window.configure(bg="pink")

ui = UserInterface(window)
ui.start()
window.mainloop()

