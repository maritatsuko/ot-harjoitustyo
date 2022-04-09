from tkinter import Tk, ttk, constants

class LoginUI:
    def __init__(self, root):
        self._root = root
    
    def start(self):
        heading_label = ttk.Label(master=self._root, text="Hi! Welcome to Mochi, please log in:")
        username_label = ttk.Label(master=self._root, text="Username: ")
        un_entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Log in")

        #checkbutton = ttk.Checkbutton(master=self._root, text="Checkbutton")
        #radiobutton = ttk.Radiobutton(master=self._root, text="Radiobutton")
        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        un_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(row=3, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
       
        #checkbutton.pack(side=constants.LEFT)
        #radiobutton.pack(side=constants.RIGHT)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)


window = Tk()
window.title("Mochi - Log in")

ui = LoginUI(window)
ui.start()
window.mainloop()