import os

directory_path = r'F:\C & C++\Python\Txt'
current_line_number=0

files = os.listdir(directory_path)
file_paths = [os.path.join(directory_path, file) for file in files]
number=1 

List_pass=[]
List_fail=[]
for file_path in file_paths:
   
 with open(file_path, 'r') as file:
     found=False
     sf=False
     for current_line_number,line in enumerate(file,1):
         val=line.replace("\n","")
         
         if current_line_number==3:
            name=val
         if val=="Soft Skills" and sf==False:
                num=current_line_number
                found=False
                count=0
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==2:
                            if val=="PASS":
                                List_pass.append(name)
                            if val=="FAIL":
                                List_fail.append(name)
                            sf=True
                            break
                    if val=="3":
                       found=True
                    if found==True:
                        count=count+1
     number=number+1
for x in range(len(List_pass)):
    print(List_pass[x])
print("Total Pass :"+str(len(List_pass))+"\n")  
print("fail :"+str(len(List_fail))+"\n") 
for x in range(len(List_fail)):
    print(List_fail[x])
      
                    
                   
       
                 