import pandas as pd

# Specify the file path
excel_file_path = 'SampleWork.xlsx'

# Read the first and last columns, skip row 2, set row 2 as header
df = pd.read_excel(excel_file_path, sheet_name='Sheet1', usecols=[0, -1], skiprows=[1], header=1)

# Display the DataFrame
print(df)

# Export the DataFrame to a new sheet 'NewSheet'
df.to_excel(excel_file_path, sheet_name='NewSheet', index=False)
