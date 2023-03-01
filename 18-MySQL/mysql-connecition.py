"""
import mysql.connector

mydb=mysql.connector.connect(    --server baglantısı--
    host="localhost", #192.23.54.55
    user="root",
    password="mysql1234"
    database="mydatabase" -hangi db kullanacagımız-
)

mycursor=mydb.cursor()  --db olusturma--
mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES") -DB leri getirir

mycursor.execute("CREATE TABLE customers (name VARCHAR(255),adress VARCHAR(255))")

 """