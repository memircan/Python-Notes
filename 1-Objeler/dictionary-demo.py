"""
ogrenciler = {
    "120" : {
        "ad":"Emircan",
        "soyad":"Tamer",
        "telefon":"123456" },
    "125":{
        "ad":"mustafa",
        "soyad":"Tamerr",
        "telefon":"12345216" },  
    "128":{"ad":"mustafa",
        "soyad":"Tamerr",
        "telefon":"12345216" },       
}

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle 
   dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
"""

ogrenciler ={}

number= input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname= input("Öğrenci soyadı: ")
phone= input("Öğrenci Tel: ")

# ogrenciler[number] = {
#     "Ad": name,
#     "soyad": surname,
#     "telefon" : phone
# }

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print(ogrenciler)
print("*"*50)

OgrNo = input("Öğrenci no: ")
ogrenci = ogrenciler[OgrNo]
print(ogrenci)

print(f"Aradığınız {OgrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']}" )