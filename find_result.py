import os

directory_path = 'F:\C & C++\Result_Analyser\Txt'
current_line_number=0

files = os.listdir(directory_path)
file_paths = [os.path.join(directory_path, file) for file in files]
am_pass=[]
am_fail=[]

dms_pass=[]
dms_fail=[]

ds_pass=[]
ds_fail=[]

cn_pass=[]
cn_fail=[]

mic_pass=[]
mic_fail=[]

cp_pass=[]
cp_fail=[]

sk_pass=[]
sk_fail=[]


for file_path in file_paths:
    
 with open(file_path, 'r') as file:
    mark_list=[]
    ap=False
    dms=False
    cn=False
    ds=False
    mic=False
    c=False
    sf=False
    for current_line_number, line in enumerate(file, 1):
            
            val=line.replace("\n","")
            if current_line_number==3:
                print(line.replace("\n",""))
            if current_line_number==9:
                print(line)
                name=line
            if val=="Applied Mathematics"and ap==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2:
                            print("("+val+")"+"- Applied Mathematics      : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                am_pass.append(name)
                            if val=="FAIL":
                                am_fail.append(name)
                            ap=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                    if found==True:
                        count=count+1
                 
            if val=="Discrete Mathematical Structures" and dms==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2:
                            print("("+val+")"+"- Discrete Mathematical    : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                dms_pass.append(name)
                            if val=="FAIL":
                                dms_fail.append(name)
                            dms=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
                        
                        
            if val=="Data Structures" and ds==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2:
                            print("("+val+")"+"- Data Structures          : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                ds_pass.append(name)
                            if val=="FAIL":
                                ds_fail.append(name)
                            ds=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
                        
            if val=="Computer Networks - I" and cn==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2: 
                            print("("+val+")"+"- Computer Networks - I    : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                cn_pass.append(name)
                            if val=="FAIL":
                                cn_fail.append(name)
                            cn=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
                        
            if val=="Microprocessors" and mic==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2: 
                            print("("+val+")"+"- Microprocessors          : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                mic_pass.append(name)
                            if val=="FAIL":
                                mic_fail.append(name)
                            mic=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
                                                           
            if val=="C Programming" and c==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2: 
                            print("("+val+")"+"- C Programing             : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                cp_pass.append(name)
                            if val=="FAIL":
                                cp_fail.append(name)
                            c=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
                        
            if val=="Soft Skills" and sf==False:
                num=current_line_number
                found=False
                result=""
                count=0
                mr=""
                for num,line in enumerate(file,1):
                    val=line.replace("\n","")
                    if found:
                        if count==1:
                            mr=val
                        if count==2: 
                            print("("+val+")"+"- Soft Skills              : "+mr)
                            mark_list.append(int(mr))
                            if val=="PASS":
                                sk_pass.append(name)
                            if val=="FAIL":
                                sk_fail.append(name)
                            sf=True
                            break
                    if val=="PASS":
                       found=True
                    elif val=="FAIL":
                        found=True
                        result="fail"
                    if found==True:
                        count=count+1
    print(mark_list)
    total=sum(mark_list)
    print("              Total is   :"+str(total)+"\n")
    
print("Aplied Math fail :"+str(len(am_fail))) 
print("Aplied Math pass :"+str(len(am_pass))+"\n") 

print("Descret math fail :"+str(len(dms_fail))) 
print("Descret Math pass :"+str(len(dms_pass))+"\n")

print("Data structure fail :"+str(len(ds_fail))) 
print("Cata structure pass :"+str(len(ds_pass))+"\n")

print("Computer network fail:"+str(len(cn_fail))) 
print("Computer network pass :"+str(len(cn_pass))+"\n")

print("Microprocessor fail:"+str(len(mic_fail))) 
print("Microprocessor pass :"+str(len(mic_pass))+"\n")

print("C programing fail:"+str(len(cp_fail))) 
print("C programing pass :"+str(len(cp_pass))+"\n")

print("Soft skill fail:"+str(len(sk_fail))) 
print("Soft skill pass :"+str(len(sk_pass))+"\n")