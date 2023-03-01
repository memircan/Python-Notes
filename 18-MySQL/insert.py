"""
import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(
        host"localhost",
        user="root",
        password="sifre",
        database="db adı")
    cursor=connection.cursor()

    sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)  %s=yer tutucu
    values=(name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursorr.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id:{cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database baglantısı kapandı")
    
def insertProducts(list):
    connection=mysql.connector.connect(
        host"localhost",
        user="root",
        password="sifre",
        database="db adı")
    cursor=connection.cursor()

    sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)  %s=yer tutucu
    values=list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursorr.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id:{cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database baglantısı kapandı")    

list=[]
while True:
    name=input("ürün adı: ")
    price=float(input("fiyat: "))
    imageUrl=input("image url: ")
    description=input("description: ")

    list.append((name,price,imageUrl,description))

    result=input('devam etmek istiyormusunuz (e/h)')
    if result == 'h':
        print("kayıtlarınız veritabanın aktarılıyor")
        print(list)
        insertProducts(list)
        break



insertProduct(name,price,imageUrl,description)
""" 