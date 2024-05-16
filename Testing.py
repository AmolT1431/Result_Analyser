from Result import *

plist=getlist()
# for item in plist:
#     print(item[0] +":"+str(item[1])+"\n")
    
sorted_people = sorted(plist, key=lambda x: x.Total,reverse=True)
print(sorted_people.__len__())


for item in sorted_people:
    print(item.Name)
    

 