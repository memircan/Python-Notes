#sayilar=[1,3,5,7,9,12,19,21]

#1- sayilar listesini while döngüsü ile yazdırın
"""
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1    
"""

#2: baslangıc ve bitis degerlerini kullanıcıdan alıp arkadaki 
#   tüm tek sayıları ekrana yazdırın.
"""
baslangıc = int(input("Başlangıç: "))
bitis= int(input("bitiş: "))

i=baslangıc
while i<bitis:
    i += 1
    if (i %2==1):
        print(i)
"""



#3- 1-100 arasındakşi sayiları azalan sekilde yazdırın.
"""
x=100
while x>0:
    print(x)
    x=x-1
"""

#4- kullanıcıdan alacagınız 5 sayıyı ekrana sıralı bir sekilde yazdırın
"""
numbers=[]
i=0
while (i<5):
    sayi=int(input("Bir sayı girniiz:"))
    numbers.append(sayi)
    i += 1
    numbers.sort()
print(numbers)
"""  

#5 kullanıcıdan alacagınız sınırsız ürün bilgisini urunler listesi icinde saklayın
#  ** ürün sayısını kullanıcıya sorun.
#  ** dictionary listesi yapısı (name,price) seklinde olsun.
#  **ürün ekleme işlemi bittiginde ürünler iekranda while ile listeleyin.

adet= int(input('Ürün adeti giriniz: '))
i=0
urunler = []

while (i<adet):
    name = input("ürün ismi: ")
    price= input("ürün fiyatı:")
    urunler.append({
        'name': name ,
        'price': price
    })
    i += 1



for urun in urunler:
    print(f'Ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}') # Dışarıda tek tırnak ise içeride çift tırnak kullanılmalı