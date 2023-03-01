#1-Girilen 2 sayıdan hangisi büyüktür?

# sayi1 = input("Bir sayı giriniz:")
# sayi2 = input("Bir sayı daha giriniz:")

#result= sayi1 > sayi2 

    
    








#2-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse gecti degilse kaldı yazdırın
# vize1=float(input("1. vize notunu girin:"))
# vize2=float(input("2. vize notunu girin:"))
# final=float(input("Final notunu giriniz:"))

# ortalama=((vize1 + vize2)/2 *0.6) + (final*0.4)
# print(f"Ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50} ")
   

#  Eğer ortalama 50 ve üstündeyse gecti degilse kaldı yazdırın
#3- girilen bir sayının tek mi çiftmi oldugunu yazdırın.
#4 girilen bir sayının negatif mi pozitifmi oldugunu yazdırın.
#5- parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
# (email: email@emircantamer.com parola:abc123)

email= "email@emircantamer.com"
password="abc123"

girilenEmail = input("email: ")
girilenPassword = input("parola: ")

isEmail = (email== girilenEmail.lower().strip())
isPassword= (password== girilenPassword )

print(f"Girilen email {isEmail} ve parola {isPassword}")