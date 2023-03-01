numbers=[1,10,5,16,4,9,10]
letters=["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val= numbers[3:6]
val= numbers[:3]
val= numbers[4:]
print(val)

numbers[4]= 40

numbers.append(49) #liste sonuna 49 ekledi
numbers.insert(3, 78) #3. indeksin yerine 78i ekledi . yani 2.den sonraya

numbers.pop() #silme metodu. hani indeksi girersek ordaki terimi siler
numbers.remove(49) #silme metodu. paranteze yazdıgımız terimi bulup siler.

numbers.sort() #kücükten büyüğe sıraladı
letters.sort() #alfabetik olarka sıraldı

numbers.reverse() #sıralamayı tersine çevirdi



print(numbers)
print(letters)

print(len(numbers))

print(numbers.count(10)) #numbers üzerinde kaç tane 10 var

numbers.clear() #bütün elemanları siler
print(numbers)