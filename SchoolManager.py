import tkinter as tk
import json
from School import School
from tkinter import Button, Canvas, Label
from PIL import ImageTk, Image
from os import path
from functools import partial

class SchoolManager():
    def __init__(self, root, filename='./컴퓨팅적사고/재직자전형소개프로그램/data/school_data.json'):
        self.root = root
        self.schools = []
        self.basePath = path.dirname(path.realpath(__file__))
        self.schoolDict = []
        
        self.filename = filename
        self.load_data()
        self.create_main_frame()
        self.create_detail_frame()
        self.create_detail_widgets()
        self.create_details_button_frame()
        
    def create_main_frame(self):

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        column, row = 0, 0
        columnCnt = 3;

        for school in self.schools:
            schoolCnt = column + row * columnCnt
    
            logoPath = school.logoPath
            name = school.name

            logoImage = Image.open(self.basePath + logoPath)
            logoImage = logoImage.resize((259, 250), Image.ANTIALIAS) 

            logo = ImageTk.PhotoImage(logoImage)

            canvas = Canvas(self.main_frame)
            canvas.grid(column=column, row=row)

            button = Button(canvas, command=partial(self.read, schoolCnt))
            button.image = logo
            button.config(image=logo)
            button.pack()

            Label(canvas, text=name).pack()

            column += 1
            if column >= columnCnt: column = 0; row += 1;
    
    def create_detail_frame(self):

        self.details_frame = tk.Frame(self.root)
        self.details_frame.pack_forget() 

        self.details_frame.grid_rowconfigure(0, weight=1)
        self.details_frame.grid_rowconfigure(1, weight=1)
        self.details_frame.grid_rowconfigure(2, weight=1)
        self.details_frame.grid_rowconfigure(3, weight=1)
        self.details_frame.grid_rowconfigure(4, weight=1)
        self.details_frame.grid_rowconfigure(5, weight=1)
        self.details_frame.grid_columnconfigure(0, weight=1)
        self.details_frame.grid_columnconfigure(1, weight=8)
        self.details_frame.grid_columnconfigure(2, weight=30)

    def create_detail_widgets(self):

        # Create Name label and entry field
        self.details_name_label = tk.Label(self.details_frame, text="학교명")
        self.details_name_label.grid(row=0, column=0, sticky='e')
        self.details_name_entry = tk.Text(self.details_frame, height=2)
        self.details_name_entry.grid(row=0, column=1, sticky='w')

        # Create Department label and entry field
        self.details_department_label = tk.Label(self.details_frame, text="학과")
        self.details_department_label.grid(row=1, column=0, sticky='e')
        self.details_department_entry = tk.Text(self.details_frame, height=2)
        self.details_department_entry.grid(row=1, column=1, sticky='w')

        # Create Obligation label and entry field
        self.details_obligation_label = tk.Label(self.details_frame, text="재직의무")
        self.details_obligation_label.grid(row=2, column=0, sticky='e')
        self.details_obligation_entry = tk.Text(self.details_frame, height=2)
        self.details_obligation_entry.grid(row=2, column=1, sticky='w')

        # Create Link label and entry field
        self.details_link_label = tk.Label(self.details_frame, text="입학처 링크")
        self.details_link_label.grid(row=3, column=0, sticky='e')
        self.details_link_entry = tk.Text(self.details_frame, height=4)
        self.details_link_entry.grid(row=3, column=1, sticky='w')

        # Create Location label and entry field
        self.details_location_label = tk.Label(self.details_frame, text="위치")
        self.details_location_label.grid(row=4, column=0, sticky='e')
        self.details_location_entry = tk.Text(self.details_frame, height=20)
        self.details_location_entry.grid(row=4, column=1, sticky='w')

    def create_details_button_frame(self):

        self.details_button_frame = tk.Frame(self.details_frame)
        self.details_button_frame.grid(row=5, column=0, columnspan=3)

        self.back_button = tk.Button(self.details_button_frame, text="뒤로가기", command=self.back)
        self.back_button.pack(side="left")

    def back(self):
        self.details_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def read(self, index):

        school = self.schools[index]

        self.details_name_entry.config(state='normal')
        self.details_department_entry.config(state='normal')
        self.details_location_entry.config(state='normal')
        self.details_obligation_entry.config(state='normal')
        self.details_link_entry.config(state='normal')

        self.details_name_entry.delete('1.0', 'end')
        self.details_department_entry.delete('1.0', 'end')
        self.details_location_entry.delete('1.0', 'end')
        self.details_obligation_entry.delete('1.0', 'end')
        self.details_link_entry.delete('1.0', 'end')

        self.details_name_entry.insert('1.0', school.name)
        self.details_department_entry.insert('1.0', school.department)
        self.details_location_entry.insert('1.0', school.location)
        self.details_obligation_entry.insert('1.0', school.obligation)
        self.details_link_entry.insert('1.0', school.link)

        self.details_name_entry.config(state='disabled')
        self.details_department_entry.config(state='disabled')
        self.details_location_entry.config(state='disabled')
        self.details_obligation_entry.config(state='disabled')
        self.details_link_entry.config(state='disabled')


        self.main_frame.pack_forget()
        self.details_frame.pack()

    def load_data(self):
        try:
            with open(self.filename, 'r') as s:
                self.schools = [School(**data) for data in json.load(s)]
                print(self.schools)
        except FileNotFoundError:
            pass