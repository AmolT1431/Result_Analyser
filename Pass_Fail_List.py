import os
from App.Student import *
from App.Config import *
from Stat_Model import *


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

def getlist():
    Student_list=[]
    
    for file_path in file_paths:
        student=Student()
        st_name=""
        list_sub=[]
        
        with open(file_path, 'r') as file:
            mark_list=[]
            subject_list=[]
            
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
                        
                        st_name=line.replace("\n","")
                        student.Name=line.replace("\n","")#for student name
                       
                    if current_line_number==9:
                        name=line
                        student.Prn=line
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
                                   # print("("+val+")"+"- Applied Mathematics      : "+mr)
                                    sub="Applied Mathematics"
                                    subject_list.append([sub,mr,val])
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
                                  #  print("("+val+")"+"- Discrete Mathematical    : "+mr)
                                    subject_list.append(["Discrete Mathematical",mr,val])
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
                                    #print("("+val+")"+"- Data Structures          : "+mr)
                                    subject_list.append(["Data Structures",mr,val])
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
                                  #  print("("+val+")"+"- Computer Networks - I    : "+mr)
                                    subject_list.append(["Computer Networks - I",mr,val])
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
                                   # print("("+val+")"+"- Microprocessors          : "+mr)
                                    subject_list.append(["Microprocessors",mr,val])
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
                                   # print("("+val+")"+"- C Programing             : "+mr)
                                    subject_list.append(["C Programing ",mr,val])
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
                                   # print("("+val+")"+"- Soft Skills              : "+mr)
                                    subject_list.append(["Soft Skills",mr,val])
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
            student.Total=sum(mark_list)
            student.Subject_list=subject_list
              
        Student_list.append(student)
    return Student_list
 
def stat_list():
    stat_list=[]
    pass_list=[len(am_pass), len(dms_pass), len(ds_pass), len(cn_pass), len(mic_pass), len(cp_pass), len(sk_pass)]
    fail_list=[len(am_fail), len(dms_fail), len(ds_fail), len(cn_fail), len(mic_fail), len(cp_fail), len(sk_fail)]
    subjects = ['M3', 'DMS', 'DSA', 'CN-I', 'MIC', 'CP', 'SS']
    stat_list.append([fail_list,pass_list,subjects])
    return stat_list
