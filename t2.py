from percentage import *

plist=getlist()
# for item in plist:
#     print(item[0] +":"+str(item[1])+"\n")
    
sorted_people = sorted(plist, key=lambda x: x[1],reverse=True)

print(sorted_people)