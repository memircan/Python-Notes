# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""
def yazdir(kelime,adet):
    print(kelime * adet)

yazdir("Merhaba\n",5)
"""

# 2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeeye çeviren fonksiyon yazın
"""
liste=[]
def listeyeCevir(*params):
    
    for param in params:
        liste.append(param)

    return liste

result=listeyeCevir(10,20,30,"Merhaba")
print(result)
"""


# 3- gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
"""


def asalSayıBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi >1:
            for i in range(2,sayi):
                if (sayi %i==0):
                    break
            else:
                print(sayi)

sayi1=int(input("sayi1=:"))
sayi2=int(input("sayi2=:"))

asalSayıBul(sayi1,sayi2)

"""


# 4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dondur

def tamBolenBulma(x):
    tamKatı=[]
    for i in range(1,x+1):
        if (x % i ==0):
            tamKatı.append(i)
    return tamKatı

sayi=int(input("sayi: "))

print(tamBolenBulma(sayi))            

