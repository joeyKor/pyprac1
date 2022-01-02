import time
import os
import pyexcel as px
import pyexcel.cookbook as PC
import sys

print ("Process Start")

start_time = time.time()

directory = sys.argv[1]
temp_file_name = "temp.csv"

outfile_name = "last_ID.xlsx"

temp_file = open(temp_file_name, 'w', encoding="utf-8")

input_files = os.listdir(directory)
headers =[]

outfile_has_header = False
for filename in input_files:
    if ".txt" not in filename:
        continue
    
    file = open(directory + "/" + filename)

    contents=[]

    for line in file:
        if ":" in line:
            splits = line.split(":")
            contents.append(splits[-1].strip())

            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    if not outfile_has_header:
        header =",".join(contents)
        temp_file.write(header)
        outfile_has_header=True

    new_line =",".join(contents)
    temp_file.write("\n" + new_line)

    file.close()

temp_file.close()

PC.merge_all_to_a_book([temp_file_name], outfile_name)

os.remove(temp_file_name)

print("process_done")

