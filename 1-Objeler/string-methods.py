message="Hello there. My name is Emircan Tamer"

#message=message.upper() #metindeki bütün harfleri büyük yapar
#message=message.lover() #kücük yapar
#message=message.title() #her kelime baş harfi büyük harfe dönüşür
#message=message.capitalize() #sadece ilk kelimedeki ilk harf büyür
#message=message.strip() #parantezde ne varsa onu siler(parola girme kısımları vb.)
#message=message.split() #her kelime tek tek farklı eleman olarak ele alınır . parantez içine ne koyarsak ordan ayırır.
#message=" ".join(message) # ayrılmış kelime gruplarını birleştirir

index= message.find("Emircan") #kelimeyi cümle icinde arar.bulunca kelimenin ilk harfindeki index numarasını söyler. kelime yoksa -1 değeri yazar.

# print(index)
# isFound=message.startswith("H") #" " ilemi başlıyor metodu . H ile başladıgı icin sonuc True cıkar
# isFound=message.endswith("r") #" " ilemi bitiyor metodu

# message=message.replace("Emircan", "Mustafa") #Cümledeki verileri değiştirir
# message=message.replace(" ","*")  #örneğin url oluştururken türke karkater yerine ingilizce karakter değiştirmesi yapılabilir

#message=message.center(100) #mesajı ortalama





print(message)




#print(message)
#print(message[2])