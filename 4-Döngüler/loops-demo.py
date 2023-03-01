"""
    1-100 arasında rastgele üretilecek bir sayıyı aşagı yukarı ifadeleri ile buldurmaya calışın.

    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

random()
Bu bize 0 <= n < 1.0 aralığında bir sayı döner.

uniform(min,max)
Bu bize min + (max — min) * random() işlemi sonucunda float bir sayı döner.

randint(min,max)
Min ve max aralığında integer olan bir sayı döner. Max dahildir. min <= n <= max

randrange(min,max)
Min ve max aralığında max dahil olmayan bir sayı döner. min <= n < max

sample(liste,q)
Liste içinde q adet rastgele değeri döner.
>>> sayilar = range(50)
>>> random.sample(sayilar,3)
[1, 19, 16]

shuffle(list)
Verdiğiniz bir liste içindeki değerlerin sırasını karıştırır.

choice(list)
Verdiğiniz bir liste içinden rastgele bir değer seçer.

"""
import random 

sayi=random.randint(1,100)
print(sayi)
print("Sayı Tahmin Oyununa hoşgeldiniz kaç adet deneme hakkı istersiniz:" ) 
#hak=int(input())
can=int(input("Kaç hak kullanmak istersiniz: "))
hak=can
sayac=0


while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("bir sayı giriniz: "))

    if sayi==tahmin:
        print(f"Tebrikler {sayac}.denemede bildiniz.Toplam puanınız:{100-(100/can)*(sayac-1)} ")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("Aşağı")
    
    if hak==0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")
    