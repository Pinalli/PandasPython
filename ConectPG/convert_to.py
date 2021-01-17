import csv

import pandas as pd
'''
read_file = pd.read_csv('clientes.csv')
read_file.to_excel('name.xlsx', index=None, header=True)
'''
df = pd.read_csv('clientes.csv')
print(df)
df.to_excel('clientesExcel.xlsx', index=None, header=True, encoding='utf-8')



#with open('clientes.csv', newline='', encoding='utf-8') as f:
 #  reader = csv.reader(f)
