from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class myFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        fig = plt.Figure(figsize=(14, 7))

        # Add subplot
        ax = fig.add_subplot(111)

        # Data
        Fail = [42,40,43,46,38,64,64]
        Pass = [25,27,24,21,29,3,3]
        subjects = ['M3', 'DMS', 'DSA', 'CN-I', 'MIC', 'CP', 'SS']

        # Plotting the bar chart
        br1 = np.arange(len(Pass))
        br2 = [x + 0.2 for x in br1]

        ax.bar(br1, Pass, color ='r', width = 0.2, edgecolor ='grey', label ='Pass')
        ax.bar(br2, Fail, color ='g', width = 0.2, edgecolor ='grey', label ='Fail')

        # Adding data labels
        for i, count in enumerate(Pass):
            ax.text(i, count + 0.5, str(count), ha='center')
        for i, count in enumerate(Fail):
            ax.text(i+0.2, count + 0.5, str(count), ha='center')

        # Setting the x-axis ticks and labels
        ax.set_xticks([r + 0.1 for r in range(len(Pass))])
        ax.set_xticklabels(subjects)
        ax.set_yticks(np.arange(0, 90, 5))

        # Adding labels and title
        ax.set_xlabel('Subjects', fontweight ='bold', fontsize = 15)
        ax.set_ylabel('Number of Students', fontweight ='bold', fontsize = 15)
        ax.set_title("Students Pass & Fail Bar")
        ax.legend()

        # Convert Matplotlib figure to Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # Add canvas to Tkinter window
        canvas.get_tk_widget().pack()
       
        
   
         
