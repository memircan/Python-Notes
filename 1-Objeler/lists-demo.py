#1- "BMW , Mercedes, Opel, Mazda" eşeöanşarona sahip bir liste oluşturunuz.
markalar=["Bmw" , "Mercedes" , "Opel" , "Mazda"]
print(markalar)

#2- Liste kaç elemanlıdır?
print(len(markalar))

#3- Listenin ilk ve son elemanı nedir?
ilkveson= markalar[0] + "," + markalar[-1]
# print(markalar[0])
# print(markalar[3])
print(ilkveson)
#4- Mazda değerini Toyota ile değiştirin.
markalar[-1]="Toyota"

print(markalar)




#5- Mercedes listenin elemanımıdır ?

isFind=markalar.index("Mercedes") #Yok ise hata verir bu yüzden listelerde 2.yazdıığım yapılır
isFind="Mercedes" in markalar
print(isFind)

#6- Listenin -2 indeksindeki değer nedir?

index=markalar[-2]
print(index)


#7- Listein ilk 3 elemanını alın.

print(markalar[0:3])

#8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekelyin 

markalar[-2:]=["Toyota","Renault"]
print(markalar)




#9- Listenin üzerine audi ve nissan değerlerini ekleyin.
markalar2=["Audi" , "Nissan"]

totalList= markalar2 + markalar
print(totalList)

#10- listenin sonelemanını silin

del markalar[-1]
print(markalar)
#11- liste elemanlarını tersten yazdırın

reverse=markalar[::-1]
print(reverse)

#12- Aşağıdaki verileri bir liste içinde sakalyınız.
    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA=["Yiğit","Bilgi", 2010, [70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan", 1998, [80,70,90]]

#13- Liste elemanlarını ekrana yazdırınız.
result= studentA[0]
result= studentB[1]
result= studentC[3][1]

result= f"{studentA[0]} {studentA[1]} {2020 - studentA[2]} yaşında ve not ortalaması { int((studentA[3][0]+studentA[3][1]+studentA[3][2])/3)}"


print(result)