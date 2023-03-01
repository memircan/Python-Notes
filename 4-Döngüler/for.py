number= [1,2,3,4,5]

for num in number: #listenin içerisinden tek tek elemanları al "num"
    print(num)     # değişkeni içerisine at döngü her döndügüne bütün sayıları ekrana yazdırıyor.
                   # "num" yerine "HELLO" yazarsak 1den5 e kadar hello yazar.yani listenin eleman sayısı kadar for döngüsü döner.

names=["mustafa","emircan","tamer"]

for name in names:
    print(f"my name is {name}")


name= "Emircan tamer"

for n in name:  #her karakteri tek tek yazdırır.
    print(n)

tuple=[(1,2),(3,4),(5,6)]

for a,b in tuple:
    print(a,b)

d={'k1' :1, "k2":2, "k3":3}

for key,value  in key,value.items:  #sadece d yazarsak k1 k2 k3 verilerini ekrana yazdırır.
    print(key,value)  # .items seklinde yazarsak eleman gruplarını yazdırır.
                       #print içine ne yazarsak o gelir ister key ister value tek tek alabilriz.
