from tkinter import ttk, constants
from locus_database import check_db

class IntroView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None
        self._db_name = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Create or open existing stratigraphical \
database")
        self._entry = ttk.Entry(master=self._frame)
        button = ttk.Button(
            master=self._frame,
            text="Create / Open",
            command=lambda:[
                self._open_database_button_click(),
                self._handle_main()]
        )

        label.pack()
        self._entry.pack()
        button.pack()

    def _open_database_button_click(self):
        entry_value = self._entry.get()
        if entry_value != "":
            self._db_name = entry_value + ".db"
            check_db(self._db_name)
        else:
            print("Database name can't be left empty")
        