import pandas as pd
import xlrd
file_xls = pd.read_excel("datos.xls","sheet1")
print(file_xls)