from tkinter import Tk, ttk, constants
from locus_database import check_db

class UI_home:
    def __init__(self, root):
        self._root = root
        self._entry = None
        
    def start(self):
        label = ttk.Label(master=self._root, text="Create or open existing stratigraphical database")
        self._entry = ttk.Entry(master=self._root)
        button = ttk.Button(
            master=self._root, 
            text="Create / Open",
            command=self._open_database_button_click)

        label.grid(row=0, column=1, pady=5)
        self._entry.grid(row=1, column=1, sticky=(constants.E, constants.W),pady=5)
        button.grid(row=2, column=1,pady=5)

        self._entry.grid()
        self._root.grid_columnconfigure(1, weight=1, minsize=500)

    def _open_database_button_click(self):
        entry_value = self._entry.get()
        if entry_value != "":
            db_name = entry_value + ".db"
            check_db(db_name)
        else:
            print("Database name can't be left empty")

class UI_basic_view:
    def __init__(self, root):
        self._root = root
        self._frame = None

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Perform an action")
        
    

window = Tk()
window.title('Stratigraphy Database Manager')

ui = UI_home(window)
ui.start()

window.mainloop()