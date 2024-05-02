# Open the source file for reading
with open("F:\C & C++\Python\Txt\PRN_TXT.txt", "r") as source_file:
    # Open the destination file for writing
    with open("PRN.txt", "w") as destination_file:
        # Read each line from the source file
        for line in source_file:
            # Write the line to the destination file
            destination_file.write(line[:10]+"\n")
            
