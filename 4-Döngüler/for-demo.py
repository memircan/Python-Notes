sayilar =[1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?
'''
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)
'''

# 2- Sayilar listesindeki sayıların toplaamı kaçtır?
'''
toplam=0

for sayi in sayilar:
    toplam=toplam + sayi

print("Toplam:",toplam)
'''

# 3- Sayilar listesindeki tek sayıların karesini alınız.
'''
for sayi in sayilar:
    if(sayi%2 ==1):
        print(sayi ** 2) #kare alma
'''

# 4- Şehirlerin hangileri en fazla 5 karakterlidir?
'''
sehirler =["kocaeli","istanbul","izmir","ankara","rize"]

for sehir in sehirler:
   if (len(sehir) <=5):
       print(sehir)
'''

# 5 -ürünlerin fiytları toplamı nedir?

urunler=[
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"}
]
toplam=0
for urun in urunler:
    fiyat=int(urun["price"])
    toplam=toplam + fiyat

print(toplam)

#6- fiyatı en fala 5000 olan ürünler nelerdir

for urun in urunler:
    if (int(urun["price"]) <=5000):
        print(urun["name"])








