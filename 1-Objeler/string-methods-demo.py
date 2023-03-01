website= "http://www.sadikturan.com"
course= "Python Kursu: Baştan sona Python programlama rehberiniz (40 saat)"

# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karkaterlrini silin.
#result=" Hello World ".strip()
#result=" Hello World ".rstrip() #sağki boşluğu siler. lstrip soldaki boslugu siler.
#print(result)


#2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin

#website=website.strip("htp:/w.com") 
#print(website)

#3- "course" karkater dizisiin tüm karakterlerini kücük harf yap.

#course=course.lower()
#print(course)

#4- "website" içinde kaç tane a karakteri vardır? (count("a"))

#website=website.count("a")
#website=website.count("a",0,10) #0ile10 arasında arar
#print(website)

#5- "website"  www ile başlayıp com ile bitiyor mu?

#index= website.startswith("www")
#index=website.endswith("com")
#print(index)

#6- "website icinde "".com" ifadesi var4mı

# website=website.find(".com") aradıgımz yoksa -1 ifadesini verir
#website=website.index(".com") aradıgımız yoksa hata verir finde ile aralarındaki fark budur
#website=website.find(".com",0,10) 
# print(website)

#7- "course" içindeli, karkatei hepsi alfabetik mi (isalpha,isdigit)

#result=course.isalpha()    
#result="Hello".isalpha()
#result=course.isdigit() # karkater dizisi rakamlardan mı oluşuyor? sorusunu sorar.
#result="123456".isdigit()

#print(result)


#8- "Content" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * elkleyiniz

#message="Content".center(50,"*")
#message="Content".ljust(50,"*") #sola yaslar 
#print(message)

#9- "course" karkater dizisindeki tüm boşluk karakterlerini "-" ile değiştirin

# message=course.replace(" ","-")
# message=course.replace(" ","-",5) sadece baştan 5 karakteri değiştirmiş olur
#message=course.replace(" ","") boşlukları silmiş oldu
# print(message)

#10- "Hello World" karakter dizisiin "Wordl" ifadesini There olarak değiştirin

# message="Hello World".replace("World","There")
# print(message)

#11- "course" karkater dizisini boşluk karakterlrinden ayırın.

# result=course.split()
# result=result[2] 2.kelimeyi yazdı
# print(result)