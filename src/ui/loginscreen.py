from tkinter import Tk, ttk, constants

class LoginUI:
    def __init__(self, root):
        self._root = root
        self._un_entry = None
    
    def start(self):
        heading_label = ttk.Label(master=self._root, background="white", text="Hi! Welcome to Mochi, please log in:")
        username_label = ttk.Label(master=self._root, background="white", text="Username: ")
        self._un_entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Log in", command=self._button_click)
        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._un_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(row=3, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)     

    def _button_click(self):
       username = self._un_entry.get()
       print(f"Welcome {username}")

window = Tk()
window.title("Mochi - Log in")
window.configure(bg="pink")

ui = LoginUI(window)
ui.start()
window.mainloop()