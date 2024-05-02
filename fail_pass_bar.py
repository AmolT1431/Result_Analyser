import numpy as np
import matplotlib.pyplot as plt 



fig = plt.figure(figsize=(10, 5))

Pass = [41]
Fail = [26]

br1 = np.arange(len(Pass))
br2 = [x + 0.2 for x in br1]

plt.bar(br1, Pass, color ='r', width = 0.1, 
        edgecolor ='grey', label ='Fail') 
plt.bar(br2, Fail, color ='g', width = 0.1, 
        edgecolor ='grey', label ='Pass') 



# Setting the x-axis ticks and labels

plt.xticks([r +0.1 for r in range(len(Pass))], 
        ['Fail & Pass Student'])
plt.yticks(np.arange(0, 70, 5))



plt.xlabel('Subjects', fontweight ='bold', fontsize = 15) 
plt.ylabel('Number of Students', fontweight ='bold', fontsize = 15) 


plt.title("Students Pass Fail Bar")
plt.legend()
plt.show()
