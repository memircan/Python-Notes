"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
adı
soydı
ad+soyad
cinsiyet
tcno
dogumyılı
adres
yaş
"""

musteriAdi="Emircan"
musteriSoyad="Tamer"
musteriAdSoyad= musteriAdi + " " + musteriSoyad
cinsiyet=True #erkek
musteriTc="12345678901"
musteriDogum="2001"
musteriAdres="Kocaeli,izmit"
musteriYas=2020 - int(musteriDogum)

print(musteriYas)

"""
2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

sipariş 1 => 110 TL 
sirapiş 2 =>1100.5 TL
sirapiş 3 =>356.95 TL
"""
order1=110
order2=1100.5
order3=356.95

total=order1 + order2 + order3

print("Hesap Tutarı:",total)
print(110+1100.5+356.95)


