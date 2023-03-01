import pandas as pd
import sqlite3

df = pd.read_csv('16-Pandas\sample.csv')
df = pd.read_json('16-Pandas\sample.json',encoding="UTF-8")
df=pd.read_excel('16-Pandas\sample.xlsx')

connection = sqlite3.connect("sample.db")
df=pd.read_sql_query("SELECT * FROM students",connection)



print(df)





