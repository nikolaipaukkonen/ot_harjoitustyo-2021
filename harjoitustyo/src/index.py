from tkinter import Tk
from gui.gui import UI

def main():
    window = Tk()
    window.title('Stratigraphy Database Manager')
    window.geometry('500x300')

    ui = UI(window)
    ui.start_gui()

    window.mainloop()


if __name__ == '__main__':
    main()
