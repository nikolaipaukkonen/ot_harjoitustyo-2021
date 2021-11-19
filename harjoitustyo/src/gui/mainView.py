import tkinter as tk
from tkinter import ttk, constants, StringVar
from locus_database import create_locus
from locus import Locus

#päänäkymä, jossa syötetään tietoja eri taulukoihin

#locuksen tyyppivaihtoehdot options-valikkoon
TYPES = ["Soil", "Construction", "Cut"]

class MainView:
    def __init__(self,root,handle_intro):
        self._root = root
        self._handle_intro = handle_intro

        self._frame = None
        self._name_entry = None
        self._type_entry = None
        self._descr_entry = None
        self._thick_entry = None

        self.type_v = tk.StringVar(self._root)
        self.thick_v = tk.StringVar(self._root)
        self.thick_v.set("1")
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    def handle_add_locus_click(self):
        self.add_locus()

    def add_locus(self):
        print("Add locus button pressed")
        type_value = self.type_v.get()
        name_value = self._name_entry.get()
        descr = self._descr_entry.get()
        thick = int(self.thick_v.get())
        print(name_value)
        print(type_value)
        print(descr)
        print(thick)

        create_locus(
                type_value,
                name_value,
                descr,
                thick,
                0,
                0)
    
    def _initialize(self): #todo: create separate methods for initializing parts
        self._frame = ttk.Frame(self._root)
        label = ttk.Label(self._frame, text="Select action", font="Helvetica 15 bold")

        locusLabel = ttk.Label(self._frame, text="Create new locus")
        self._type_entry = ttk.OptionMenu(self._frame,self.type_v, TYPES[0],*TYPES)

        self._name_entry = ttk.Entry(master=self._frame)
        self._name_entry.insert(0, "Enter locus name")

        self._descr_entry = ttk.Entry(master=self._frame)
        self._descr_entry.insert(0, "Insert locus description")

        self._thick_entry = ttk.Spinbox(
                        self._frame, 
                        from_=0, 
                        to=200, 
                        textvariable=self.thick_v
                        )

        add_locus_button = ttk.Button(
            master=self._frame,
            text="Add locus",
            command=self.handle_add_locus_click()
        )

        findLabel = ttk.Label(self._frame, text="Create new find")

        add_find_button = ttk.Button(
            master=self._frame,
            text="Add find",
            #command=self._handle_add_find
        )

        sampleLabel = ttk.Label(self._frame, text="Create new sample")

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

        locusLabel.pack()
        self._type_entry.pack()
        self._name_entry.pack()
        self._descr_entry.pack()
        self._thick_entry.pack()
        add_locus_button.pack()

        findLabel.pack()
        add_find_button.pack()

        sampleLabel.pack()
        add_sample_button.pack()

        add_return_button.pack()