liste =["1","2","5a","10b","abc","10","50"]

# 1-Liste elemanları içindeki sayısal değerleri bulunuz.
"""
sayilar=[]
for x in liste:
    try:
        result=int(x)        
    except ValueError:
        continue
    else:
        sayilar.append(result)
print(sayilar)
"""

# 2-Kullanıcı "q" değerini girmedikce aldıgınız her inputun sayı oldugundan emin olunz
#aksi halde hata mesajı yazın.

sayilar=[]
print("istediğiniz kadar sayı giriniz. Sayı girme işlemini sonlandırmak için 'q' harfine basınız")
while True:
    x=input("Sayı giriniz: ")
    if x == "q":
        print("Sayı girme işlemi bitmiştir")
        break
    
    try:
        sayi=int(x)
    except ValueError:
        print("Gecersiz sayı")
        continue
    else:
        sayilar.append(sayi)

print(f"Girdiğiniz sayilar {sayilar}")

"""   
# 3-Girilen parola içinde türkçe karkater hatası veriniz.

def check_password(parola):
    turkce_karakterler= "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")
        else:
            pass
    print("geçerli parola")

parola=input("Parola: ")

try:
    check_password(parola)
except TypeError as err:
    print(err)







# 4-Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin hata mesajları verin.S
"""