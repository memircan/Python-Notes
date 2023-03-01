names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998, 2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

#2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)

#3- "Deniz" ismini listeden siliniz.
#names.remove("Deniz")
#names.pop(4) aynı işlev sadece index sayısını yazarak sildi


#4-"Deniz" isminin indeksi nedir?
index= names.index("Deniz")

print(index)

#5- "Ali" listenin bir elemanımıdır?

isFind="Ali" in names
print(isFind)

#6- Liste elemanlarını ters çevirin.

names.reverse()
print(names)

#7- Liste elemanlarını alfabetir olarak sıralayınız.

names.sort()
print(names)

#8- years listesini rakamsal büyüklüper göre sıralayınız.

years.sort()
print(years)

#9 - str="Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str="Chevroler, Dacia"

carlist=str.split(",")
print(carlist)

#10- years dizisini en büyük ve en kücük elemanı nedir?

Min=min(years)
Max=max(years)

print(Min,Max)

#11- years dizisiinde kac tane 1998 değeri vardr.
result=years.count(1998)
print(result)

#12- years dizsiin tüm elemanlarını siliniz.

years.clear()
print(years)

#13- kullanıcıdan alacagınız 3 tane marka bilgisin bir lsitede saklayınız

markalar= []

marka = input("1.Marka: ")
markalar.append(marka)

marka = input("2.Marka: ")
markalar.append(marka)

marka = input("3.Marka: ")
markalar.append(marka)

print(markalar)