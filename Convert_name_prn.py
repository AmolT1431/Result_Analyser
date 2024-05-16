import os

# Directory path
directory_path = r'F:\C & C++\Result_Analyser\Txt'

files = os.listdir(directory_path)


file_paths = [os.path.join(directory_path, file) for file in files]

for file_path in file_paths:
    name_r=''
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, 1):
            if current_line_number ==9:
                val=line.replace("\n","")
                name=line
                name_r=name.replace("\n","")
                print(name)
                
    file.close   
    ex=".txt"
    file_path_n = 'F:\C & C++\Result_Analyser\Txt'+'\\'+name_r+ex  
    os.rename(file_path,file_path_n)