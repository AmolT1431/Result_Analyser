import tkinter as tk
from tkinter import ttk
from Result import *

class List_Prn:
    def __init__(self,frame):
        self.style = ttk.Style()
        self.style.configure("Custom.Treeview", rowheight=30, font=('Times New Roman', 20, 'bold'))
        self.style.configure("Custom.Treeview.Heading", font=('Times New Roman', 14, 'bold')) 
        
        
        self.table = ttk.Treeview(frame,columns=('Name','Prn'),show='headings',style="Custom.Treeview")
        self.table.heading('Name',text = 'Name')
        self.table.heading("Prn",text = 'Prn No.')
        
        self.table.column('Name',width=110)
        self.table.column('Prn',width=300, anchor='center',stretch=True)
        
        mylist = getlist()
        self.table.tag_configure("gray",background="lightgray")
        self.table.tag_configure("normal",background="white")
        my_tag="normal"
        
        for item in mylist:
            if(my_tag=="gray"):
               my_tag='normal'
            else:
               my_tag='gray'
            self.table.insert(parent='',index=0,values=(item.Name,item.Prn),tags=(my_tag))
        
        self.table.pack(fill="both",expand=True)