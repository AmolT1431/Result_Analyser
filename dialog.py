import tkinter as tk
from DialogBox.Folder_Select import*
import App.Config as con


# Create the main window
root = tk.Tk()
root.title("Folder Selector")
 

# Create a button to open the folder dialog
button = tk.Button(root, text="Select Folder", command=lambda:select_file(label))
button.pack(pady=20)

# Create a label to display the selected folder path
label = tk.Label(root, text='')
label.pack(pady=20)
 

# Run the Tkinter event loop
root.mainloop()
