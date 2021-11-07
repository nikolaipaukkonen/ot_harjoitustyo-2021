from tkinter import tk
from ui.ui import UI

def main():
    window = Tk()
    window.title('Stratigraphy Database Manager')

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
    main()
