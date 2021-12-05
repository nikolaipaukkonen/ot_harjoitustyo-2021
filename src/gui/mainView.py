''' Päänäkymä, jossa syötetään tietoja eri taulukoihin '''

import tkinter as tk
from tkinter import ttk, constants, StringVar
from database.locus_database import create_find, create_locus, fetch_loci, fetch_finds, fetch_locus_ids, export_data, fetch_locus_ids
from database.locus import Locus
from database.find import Find

#locuksen tyyppivaihtoehdot options-valikkoon
TYPES = ["Soil", "Construction", "Cut"]
FINDS = ["Pottery", "Lithic", "Coin", "Iron object", "Silver", \
    "Gold", "Nail", "Glass", "Bone", "Wood", "Lead"]

class MainView:
    def __init__(self,root,handle_intro): #siistittävä
        self._root = root
        self._handle_intro = handle_intro

        self._frame = None

        self.locus_ids = fetch_locus_ids()

        self._name_entry = None
        self._type_entry = None
        self._descr_entry = None
        self._thick_entry = None
        self._above_entry = None

        self.type_v = tk.StringVar(self._root)
        self.thick_v = tk.StringVar(self._root)
        self.above_v = tk.StringVar(self._root)
        self.thick_v.set("1")

        self._find_type_entry = None
        self._find_dating_entry = None
        self._find_descr_entry = None
        self._find_weight_entry = None
        self._find_locus_entry = None

        self.find_type_v = tk.StringVar(self._root)
        self.find_weight_v = tk.StringVar(self._root)
        self.find_locus_v = tk.StringVar(self._root)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def add_locus(self):
        type_value = self.type_v.get()
        name_value = self._name_entry.get()
        descr = self._descr_entry.get()
        thick = int(self.thick_v.get())
        above = int(self.above_v.get())

        locus = Locus(type_value, name_value, descr, thick, above)
        create_locus(locus)
        self.locus_ids = fetch_locus_ids()

    def add_find(self):
        find_type = self.find_type_v.get()
        dating = self._find_dating_entry.get()
        descr = self._find_descr_entry.get()
        weight = self.find_weight_v.get()
        locus = int(self.find_locus_v.get())

        find = Find(find_type, dating, descr, weight, locus)
        create_find(find)

    def _initialize_add_locus(self):
        self.locus_ids = fetch_locus_ids()

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

        self._above_entry = ttk.OptionMenu(
                        self._frame,
                        self.above_v,
                        *self.locus_ids
        )

        add_locus_button = ttk.Button(
            master=self._frame,
            text="Add locus",
            command=lambda : self.add_locus()
        )

        locusLabel.pack()
        self._type_entry.pack()
        self._name_entry.pack()
        self._descr_entry.pack()
        self._thick_entry.pack()
        self._above_entry.pack()
        add_locus_button.pack()

    def _initialize_add_find(self):
        findLabel = ttk.Label(self._frame, text="Create new find")

        self._find_type_entry = ttk.OptionMenu(self._frame,self.find_type_v, FINDS[0],*FINDS)

        self._find_dating_entry = ttk.Entry(master=self._frame)
        self._find_dating_entry.insert(0, "Enter find dating")
        self._find_descr_entry = ttk.Entry(master=self._frame)
        self._find_descr_entry.insert(0, "Enter find description")
        self._find_weight_entry = ttk.Spinbox(
                                self._frame,
                                from_=0,
                                to=10000,
                                textvariable=self.find_weight_v
                            )
        self._find_locus_entry = ttk.OptionMenu(
                self._frame,
                self.find_locus_v,
                *self.locus_ids
        )

        add_find_button = ttk.Button(
            master=self._frame,
            text="Add find",
            command=lambda : self.add_find()
        )

        findLabel.pack()
        self._find_type_entry.pack()
        self._find_dating_entry.pack()
        self._find_weight_entry.pack()
        self._find_locus_entry.pack()
        add_find_button.pack()

    def _initialize_add_sample(self): #to be implemented
        sampleLabel = ttk.Label(self._frame, text="Create new sample")

        add_sample_button = ttk.Button(
            master=self._frame,
            text="Add sample",
            #command=self._handle_add_sample
        )

        sampleLabel.pack()
        add_sample_button.pack()

    def _initialize_export_button(self):
        export_filename_label = ttk.Label(master=self._frame, text="Export locus data")
        self.export_filename = ttk.Entry(master=self._frame)
        self.export_filename.insert(0, "Enter filename")

        add_export_loci_button = ttk.Button(
            master=self._frame,
            text="Export locus data as csv file",
            command=lambda: self.handle_export()
        )

        export_filename_label.pack()
        self.export_filename.pack()
        add_export_loci_button.pack()

    def display_loci(self):
        ''' Hakee tietokannasta stratigrafiset kerrokset ja tulostaa ne näkymään '''
        rows = fetch_loci()
        display_locus_label = ttk.Label(self._frame, text="Current stratigraphical units")
        display_locus_label.pack()

        for row in rows:
            e = ttk.Entry(self._frame, width=50)
            e.insert(0, row)
            e.pack()

    def display_finds(self):
        ''' Hakee tietokannasta löydöt ja tulostaa ne näkymään '''
        rows = fetch_finds()
        display_finds_label = ttk.Label(self._frame, text="Current registered finds")
        display_finds_label.pack()

        for row in rows:
            e = ttk.Entry(self._frame, width=50)
            e.insert(0, row)
            e.pack()

    def handle_export(self):
        filename = self.export_filename.get()
        export_data(filename)

    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        label = ttk.Label(self._frame, text="Select action", font="Helvetica 15 bold")

        add_return_button = ttk.Button(
            master=self._frame,
            text="Switch project",
            command=lambda: self._handle_intro()
        )

        add_display_loci_button = ttk.Button(
            master=self._frame,
            text="Display loci",
            command=lambda: self.display_loci()
        )

        add_display_finds_button = ttk.Button(
            master=self._frame,
            text="Display finds",
            command=lambda: self.display_finds()
        )

        label.pack()

        self._initialize_add_locus()
        self._initialize_add_find()
        self._initialize_add_sample()

        add_display_loci_button.pack()
        add_display_finds_button.pack()

        self._initialize_export_button()

        add_return_button.pack()
        