class Student:
    def __init__(self):
        self.Name=""
        self.Prn=0
        self.Subject_list=[]
        
        #self.No_Fail=pass_or_fail(self.Subject_list)
        self.Total=0
        
    def Result(self):
        for sublist in self.Subject_list:
            if sublist[2] != 'PASS':
                return 'FAIL'
        return 'PASS'
    
    def fail_sub_count(self):
        failed_count = 0
        for sublist in self.Subject_list:
            if sublist[2] != 'PASS':
                failed_count += 1
        return failed_count
    
    def failed_subjects(self):
        failed_subjects = []
        for sublist in self.Subject_list:
            if sublist[2] != 'PASS':
                failed_subjects.append(sublist[0][:4])
        return failed_subjects
     
    def Subjects_Result(self):
        Subjects = []
        for sublist in self.Subject_list:
            if sublist[2] == 'PASS':
                Subjects.append([sublist[0][:4],"PASS"])
            else:
                Subjects.append([sublist[0][:4],"FAIL"])

        return Subjects   

 

    