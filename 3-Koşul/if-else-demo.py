#1- Kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

# isim= input("İsminizi giriniz: ")
# yas= int(input("Yasınızı girniiz: "))
# egitim= input("Eğitim seviyenizi giriniz: ").lower()

# if (yas>=18):
#     if (egitim=="lise") or (egitim=="üniversite"):
#         print(f"Sayın {isim} ehliyet almak için uygunsunuz.")
#     else:
#         print(f"Sayın {isim} , {egitim} eğitim seviyesi ehliyet almak için uygun değildir.")
# else:
#     print(f"sayın {isim} , {yas} yaşında olduğunuzdan ötürü ehliyet için uygun değilsiniz.")

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına
#  karşılık gelen not bilgisini yazdırınız.
# 0-24 --0
# 25-44 --1
# 45-54 --2
# 55-69 --3
# 70-84 --4
# 85-100 --5

#yazılı1= int(input("1. yazılı notunu giriniz: "))
#yazılı2= int(input("2. yazılı notunu giriniz: "))
#sözlü= int(input("sözlü notunu giriniz: "))

#int(ortalama)=(yazılı1 + yazılı2 + sözlü)/3

# 325443252523523 tane if-elif komutu ile yapılcak ugrasmaya degmez


#3- Trafiğe cıkıs tarihi alınan bir aracın servis zamanını asagıdaki bilgilere göre hesaplayın 
#   datetime modülü ile.

#1.bakım 1.yıl
#2.       2.yıl
#3.       3.yol

import datetime #modülü ilk önce cagırmamız gerek.

tarih=input("aracınız trafiğe hangi yılda çıktı (2019/8/9):  ")
tarih=tarih.split("/")

simdi = datetime.datetime.now() #bulunan zamanı yazdırır.

trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark= simdi - trafigecikis
days= fark.days

if days<=365:
    print("1.servis aralıgı")
elif days>365 and days <=365*2:
    print("2.aralık")
elif days>365*2 and days<=365*3:
    print("3.aralık")
else:
    print("hatalı süre.")
