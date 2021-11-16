import tkinter as tk
from tkinter import ttk, constants
from locus_database import create_locus
from locus import Locus

TYPES = ["Soil", "Construction", "Cut"]

class MainView:
    def __init__(self,root,handle_intro):
        self._root = root
        self._handle_intro = handle_intro
        self._frame = None

        #self.type_v = tk.StringVar()
        #self.type_v.set("Select locus type")
        #self.name_v = tk.StringVar()
        #self.thick_v = tk.StringVar()
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
 
    #def add_locus(self):
    #   locus = Locus(
    #                self.type_v.get,
    #               self.name_v.get,
    #               "placeholder",
    #               self.thick_v.get,
    #               0,
    #               0
    #           )

    #    create_locus(locus)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Select action")

        #type_entry = ttk.OptionMenu(self._frame, self.type_v, *TYPES)
        #name_entry = ttk.Entry(self._frame, self.name_v)
        #name_entry.insert(0, "Enter locus name")
        #thick_entry = ttk.Entry(self._frame, self.thick_v)

        add_locus_button = ttk.Button(
            master=self._frame,
            text="Add locus",
            #command=self.add_locus()
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
        #type_entry.pack()
        #name_entry.pack()
        #thick_entry.pack()
        add_locus_button.pack()
        add_find_button.pack()
        add_sample_button.pack()
        add_return_button.pack()