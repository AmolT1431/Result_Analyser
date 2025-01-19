from tkinter import *
from tkinter import ttk
from Result import *

class Top5_List(Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="yellow")
        
        style = ttk.Style(self)
        style.theme_use("clam")  #
        style.configure("Custom.Treeview", rowheight=25, font=('Times New Roman', 10, 'bold'))
        style.configure("Custom.Treeview.Heading", font=('Times New Roman', 14, 'bold'))  # Adjust font size for headings
        
        # Create the Treeview widget
        self.table = ttk.Treeview(self, columns=('Name', 'Marks'), show='headings', style="Custom.Treeview")
        self.table.heading('Name', text='Name')
        self.table.heading("Marks", text='Marks')
       
        
        # Set column width to center align the text
        self.table.column('Name')
        self.table.column('Marks',width=95, anchor='center',stretch=True)
         
        
        # Insert sample data
      
        mylist = getlist()
        sort=sorted(mylist, key=lambda x: x.Total,reverse=True)
         
        self.table.tag_configure("gray",background="lightgray")
        self.table.tag_configure("normal",background="white")
        my_tag="normal"
        count=1
        for item in sort:
           string=str(count)+") "+item.Name
           if(item.Result()=="PASS"):
               my_tag='normal'
           else:
               my_tag='gray'
           st=""
           for string in item.failed_subjects():
               st=st + string + ","
             
           if(my_tag=="normal"):
               self.table.insert(parent='', index=END, values=(string, item.Total),tags=(my_tag))
               count=count+1
               if(count==6):
                   break
             
               
                
        self.table.pack(fill="both", expand=True)
        self.grid(row=0, column=0, sticky="nsew")