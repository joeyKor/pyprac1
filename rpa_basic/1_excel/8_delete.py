from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws = wb.active


#ws.delete_rows(8)

ws.delete_cols(2)



wb.save("sameple_delete_col.xlsx")