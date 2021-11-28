import os
from tkinter import Tk
from gui.gui import UI

def main():
    #luo väliaikaisen muistin session tietokannoille
    f = open("db_list", "w+")

    window = Tk()
    window.title('Stratigraphy Database Manager')
    window.geometry('500x1000')

    ui = UI(window)
    ui.start_gui()

    window.mainloop()

    #poistaa väliaikaisen tietokantamuistin
    os.remove("db_list")


if __name__ == '__main__':
    main()
