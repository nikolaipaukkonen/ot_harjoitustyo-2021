''' Käynnistää ohjelman graafisen käyttöliittymän '''

import os
from tkinter import Tk
from gui.gui import UI

def main():
    ''' Ohjelman main-metodi joka käynnistää käyttöliittymän ja alustaa tietokantamuistin'''
    open("db_list", "w+", encoding="utf-8")

    window = Tk()
    window.title('Stratigraphy Database Manager')
    window.geometry('1200x1000')

    ui = UI(window)
    ui.start_gui()

    window.mainloop()

    #poistaa väliaikaisen tietokantamuistin
    os.remove("db_list")


if __name__ == '__main__':
    main()
