from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

ws.append(["num", "eng", "math"])
for i in range(1,11):
    ws.append([i, randint(50,100), randint(50,100)])

wb.save("sample.xlsx")


