import pandas as pd

file = pd.ExcelFile("./pandas/sales.xls")
print(file.sheet_names)
sheet = file.parse('sales')

print(sheet)
