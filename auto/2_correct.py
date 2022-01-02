import random
import pyexcel as px

print("Process Start")

NUM_SAMPLES = 10

alphabet_samples ="abcdefghijklmnopqrstuvwxyz"

def random_stirng(length):
    result =""
    for i in range(length):
        result += random.choice(alphabet_samples)

    return result

first_name_samples ="조최강"
middle_name_samples ="이현우"
last_name_samples = "준현민"

def random_name():
    result =""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

HEADER = ["name"]

for i in range(NUM_SAMPLES):
    name = random_name()

    file_name = "personal_info/" + str(i) + name + ".xlsx"
    
    contents =[]
    contents.append(name)
    RESULT = [HEADER, contents]
    px.save_as(array = RESULT, dest_file_name = file_name)


print ("process done")
    