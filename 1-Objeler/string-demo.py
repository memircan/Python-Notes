website="http://www.sadikturan.com"
course ="Python Kursu: Baştan sona python programlama rehberiniz(40 saat)"
#1-course karakter dizisinde kaç karakter vardır
result=len(course)
length=len(website)
print(result)

#2-website içinden www karakterlerini alın
print(website[7:10])

#3-website içinden com karakterlrini alın
print(website[length-3:length])

#4-course içinden 15 ve son 15 karakterleri alın

print(course[0:15])
# print(course[:15]) ilk 15
# print(course[15:]) son 15
print(course[result-15:result]) 

#5-course ifadesindeki karakterleri tersten yazdırın
print(course[::-1])
# s="12345"*5 ==>5kez tekrar eder
# print(s[::5]) ==>5seferde bir seçer herbiri 1 sayısına denk gelir

#6-aşagıda verilen değişkenler ile ekrana asagıdaki ifadeyi yazdırın
# "Benim adım Emircan Tamer, yaşım 18 ve mesleğim mühendislik"
name, surname,age,job="Emircan"," Tamer",18,"mühendis."
#1.yol
print("Benim adım {}{} , yaşım {} ve mesleğim {}".format(name,surname,age,job))
#2.yol
result= "Benim adım " + name + surname + " yaşım " + str(age) + " ve mesleğim " + job
#3.yol
result=f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
print(result)

#7- Hello world ifadesindeli w harfini "W" ile deşiştirin 

s="Hello world"

s.replace("w","W") #Daha basit yolu 

print(s)

#- "abc" ifadesini yan yana 3 defa yadırın
x="abc "*3
print(x)
