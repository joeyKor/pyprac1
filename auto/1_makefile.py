import time
import random
import os
import pyexcel as px

print("process start")

start_time  = time.time()

NUM_SAMPLES =10

# alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"

# def random_string(length):
#     result =""
#     for i in range(length):
#         result += random.choice(alphabet_samples)
#     return result

first_name_samples = "김이박조"
middle_name_sampels = "민서예이현"
last_name_samples = "준윤우원호"

alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"

def random_name():
    result =""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_sampels)
    result += random.choice(last_name_samples)
    return result

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result

# os.mkdir("person_info")

# os.mkdir("personal_info")

HEADER = ["name", "age", "e-mail"]

for i in range(NUM_SAMPLES):
    name=random_name()
    
    filename = "personal_info/" + str(i)+"_"+ name +".xlsx"
    contents = []

    contents.append(name)

    contents.append(str(time.time())[-2:])

    contents.append(random_string(6)+"@bhban.com")

    RESULT =[HEADER, contents]
    px.save_as(array=RESULT, dest_file_name = filename)
    
    # print(RESULT)
    
    # px.save_as(array=RESULT, dest_file_name = filename)




print("process Done")
