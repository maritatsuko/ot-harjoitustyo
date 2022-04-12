from tkinter import Tk
from ui.the_ui import UserInterface

def main():
    window = Tk()
    window.title("Mochi")
    window.configure(bg="pink")

    ui = UserInterface(window)
    ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()
    