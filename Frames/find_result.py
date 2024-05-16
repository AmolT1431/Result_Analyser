import tkinter as tk
from tkinter import ttk
from Result import *

class Frame_Find_Result(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create a custom style for Treeview
        style = ttk.Style(self)
        style.theme_use("clam")  #
        style.configure("Custom.Treeview", rowheight=25, font=('Times New Roman', 10, 'bold'))
        style.configure("Custom.Treeview.Heading", font=('Times New Roman', 14, 'bold'))  # Adjust font size for headings
        
        # Create the Treeview widget
        self.table = ttk.Treeview(self, columns=('Name', 'Result', 'no.fail_sub','fail_sub', 'total'), show='headings', style="Custom.Treeview")
        self.table.heading('Name', text='Name')
        self.table.heading("Result", text='Result')
        self.table.heading("no.fail_sub", text='No. Fail')
        self.table.heading("fail_sub", text='Fail_sub')
        self.table.heading("total", text='Total')
        
        # Set column width to center align the text
        self.table.column('Name')
        self.table.column('Result',width=95, anchor='center',stretch=True)
        self.table.column('no.fail_sub',width=95, anchor='center')
        self.table.column('total', width=95,anchor='center')
        
        # Insert sample data
      
        mylist = getlist()
        sort=sorted(mylist, key=lambda x: x.Total,reverse=True)
        sort.reverse()
        self.table.tag_configure("gray",background="lightgray")
        self.table.tag_configure("normal",background="white")
        my_tag="normal"
        for item in sort:
           if(item.Result()=="PASS"):
               my_tag='normal'
           else:
               my_tag='gray'
           st=""
           for string in item.failed_subjects():
               st=st + string + ","
               
           self.table.insert(parent='', index=0, values=(item.Name, item.Result(), item.fail_sub_count(), st,item.Total),tags=(my_tag))
            
           
        self.table.pack(fill="both", expand=True)

 
