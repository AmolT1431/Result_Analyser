import tkinter as tk
from tkinter import ttk
from percentage import *

class Frame_Find_Result(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create a custom style for Treeview
        style = ttk.Style(self)
        style.configure("Custom.Treeview", rowheight=25, font=('Arial', 10, 'bold'))
        style.configure("Custom.Treeview.Heading", font=('Arial', 14, 'bold'))  # Adjust font size for headings
        
        # Create the Treeview widget
        self.table = ttk.Treeview(self, columns=('Name', 'status', 'fail_sub', 'percentage'), show='headings', style="Custom.Treeview")
        self.table.heading('Name', text='Name')
        self.table.heading("status", text='Status')
        self.table.heading("fail_sub", text='No. Fail')
        self.table.heading("percentage", text='Total')
        
        # Set column width to center align the text
        self.table.column('Name')
        self.table.column('status', anchor='center')
        self.table.column('fail_sub', anchor='center')
        self.table.column('percentage', anchor='center')
        
        # Insert sample data
      
        mylist = getlist()
        sort=sorted(mylist, key=lambda x: x[1],reverse=True)
        sort.reverse()
   
     
        for item in sort:
           num_fails = sum(1 for element in item[2] if element != 'PASS')
           
           if all(element == 'PASS' for element in item[2]):
               result="Pass"
           else:
               result="Fail"
           if(num_fails==0):
               no=''
           else:
               no=num_fails
                
           self.table.insert(parent='', index=0, values=(item[0], result, no, item[1]))
        
        # Pack the Treeview widget
        self.table.pack(fill="both", expand=True)

 
