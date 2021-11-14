from tkinter import ttk, constants

class MainView:
    def __init__(self,root,handle_intro):
        self._root = root
        self._handle_intro = handle_intro
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Select action")

        add_locus_button = ttk.Button(
            master=self._frame,
            text="Add locus",
            #command=self._handle_add_locus
        )

        add_find_button = ttk.Button(
            master=self._frame,
            text="Add find",
            #command=self._handle_add_find
        )

        add_sample_button = ttk.Button(
            master=self._frame,
            text="Add sample",
            #command=self._handle_add_sample
        )

        add_return_button = ttk.Button(
            master=self._frame,
            text="Switch project",
            command=self._handle_intro
        )

        label.pack()
        add_locus_button.pack()
        add_find_button.pack()
        add_sample_button.pack()
        add_return_button.pack()