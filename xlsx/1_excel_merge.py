from pathlib import Path
import pandas as pd

input_folder = 'd:/data'
raw_data_dir = Path(input_folder)
excel_files = raw_data_dir.glob('*')

total_df = pd.DataFrame()

for excel_file in excel_files:
    df = pd.read_excel(excel_file)
    total_df = total_df.append(df, ignore_index=True)

merged_excel = input_folder +'/merged.xlsx'

total_df.to_excel(merged_excel, sheet_name='data merge', index=False)


print("successfull made")

