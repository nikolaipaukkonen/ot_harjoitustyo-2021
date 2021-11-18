import tkinter as tk
from tkinter import ttk, constants
from locus_database import create_locus
from locus import Locus

TYPES = ["Soil", "Construction", "Cut"]

class MainView:
    def __init__(self,root,handle_intro):
        self._root = root
        self._handle_intro = handle_intro
        self._name_entry = None
        self._type_entry = None
        self._frame = None

        self.type_v = tk.StringVar(self._root)
        self.thick_v = tk.StringVar(self._root)
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
 
    def add_locus(self):
        print("Add locus button pressed")
        type_value = self.type_v.get()
        name_value = self._name_entry.get()

        create_locus(
                type_value,
                name_value,
                "placeholder",
                13,
                0,
                0)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Select action")

        
        self._type_entry = ttk.OptionMenu(self._frame,self.type_v, TYPES[1],*TYPES)

        self._name_entry = ttk.Entry(master=self._frame)
        self._name_entry.insert(0, "Enter locus name")
        thick_entry = ttk.Spinbox(
                        self._frame, 
                        from_=0, 
                        to=200, 
                        textvariable=self.thick_v
                        )

        add_locus_button = ttk.Button(
            master=self._frame,
            text="Add locus",
            command=self.add_locus()
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
        self._type_entry.pack()
        self._name_entry.pack()
        thick_entry.pack()
        add_locus_button.pack()
        add_find_button.pack()
        add_sample_button.pack()
        add_return_button.pack()