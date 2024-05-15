from Result import *

plist=getlist()
# for item in plist:
#     print(item[0] +":"+str(item[1])+"\n")
    
sorted_people = sorted(plist, key=lambda x: x.Total,reverse=True)
print(sorted_people.__len__())

item=sorted_people[0]

print(item.Subject_list)
 


def check_result(list_of_lists):
    for sublist in list_of_lists:
        if sublist[2] != 'PASS':
            return 'FAIL'
    return 'PASS'
print(check_result(item.Subject_list))