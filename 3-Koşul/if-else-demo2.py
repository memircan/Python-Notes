'''
Girilen Bir sayının 0-100 arasına olup olmadıgını kontrol ediniz


sayi=float(input("sayı: "))


if (sayi>0) and (sayi<100):
    print("Sayı 0-100 arasındadır.")
else:
    print("Sayı 0-100 arasında değildir.")

Girilen bir sayının pozitif çift sayı olup olmadıgını knotrol ediniz.
'''

sayi= int(input("sayı: "))



if (sayi>0):
    if (sayi % 2 ==0):
        print("Girilen sayı pozitif bir çift sayıdır.")
    else:
        print("Girilen sayı pozitif bir tek sayıdır.")
else:
    if (sayi % 2 ==0):
        print("Girilen sayı negatif bir çift sayıdır.")
    else:
        print("Girilen sayı negatif bir tek sayıdır.")    