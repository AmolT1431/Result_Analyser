file_path = 'F:\C & C++\Python\Txt\PRN_TXT.txt'

with open(file_path, 'r') as file:
    for current_line_number, line in enumerate(file, 1):
            val=line[:10]
            print(val)
