import pandas as pd
from flask import Flask

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

#CSV
#dfcsv = pd.read_csv("cleaning.csv")
#use to_string() to print the entire DataFrame.

#JSON
dfjson = pd.read_json('data.json')
#para obter informações do arquivo: colunas vazias, colunas duplicadas,...
#print(dfjson.info())

#cleaning data:
#dfxlsx = pd.read_excel('datacleaning.xlsx')

#new_csv = dfxlsx.dropna()


print(dfjson.to_string())