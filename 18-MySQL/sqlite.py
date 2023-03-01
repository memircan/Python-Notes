
import sqlite3

connection =sqlite3.connect("node_app.db") #db varsa acar yoksa olusturur
cursor=connection.cursor()

cursor.execute("selec * from customers")
liste= cursor.fetchall()
print(liste)


connection.close()