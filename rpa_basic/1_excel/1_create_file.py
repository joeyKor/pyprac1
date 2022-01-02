from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성
ws = wb.active
ws.title = "itcoding"
wb.save("practice.xlsx")
wb.close