import numpy as np
import matplotlib.pyplot as plt 



fig = plt.figure(figsize=(10, 5))

Fail = [42,40,43,46,38,64,64]
Pass = [25,27,24,21,29,3,3]

br1 = np.arange(len(Pass))
br2 = [x + 0.2 for x in br1]

plt.bar(br1, Pass, color ='r', width = 0.2, 
        edgecolor ='grey', label ='Fail') 
plt.bar(br2, Fail, color ='g', width = 0.2, 
        edgecolor ='grey', label ='Pass') 



# Setting the x-axis ticks and labels

plt.xticks([r +0.1 for r in range(len(Pass))], 
        ['Applied Math ', 'Discrete Math', 'Data Structures', 'Computer Network','Microprocessor', 'C programing','Soft - skills'])
plt.yticks(np.arange(0, 90, 5))


for i, count in enumerate(Pass):
    plt.text(i, count + 0.5, str(count), ha='center')
for i, count in enumerate(Fail):
    plt.text(i, count + 0.5, str(count), ha='center')
    
plt.xlabel('Subjects', fontweight ='bold', fontsize = 15) 
plt.ylabel('Number of Students', fontweight ='bold', fontsize = 15) 


plt.title("Students Pass & Fail Bar")
plt.legend()
plt.show()
