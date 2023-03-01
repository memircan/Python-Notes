x,y,z=2,5,10

numbers=1,5,7,10,6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

# a=int(input("1.Sayı: "))
# b=int(input("2.Sayı: "))
# result = (a*b) - (x+y+z)
# print(result)

#2- y'nin x'e kalansız bölümünü hesaplayınız

#result = y // x                     # // işareti kalansız bölme işareti
#print(result)


#3- (x,y,z) toplamının mod 3 ü nedir

#print((x+y+z) % 3)                  # "%" mod alma işareti

#4- y'nin x. kuvvetini hesaplayınız

#result= y ** x                      # ikitane yıldız kuvvet işareti
#print(result)

#5-x, *y, z = numbers işlemine göre z'nin küpü kaçtır

x,*y,z = numbers
print(z**3) #küp istedigi icin 3 yazdk

#6- x,*y, z = numbers işlemine göre y'nin deüerleri toplamı kaçtır

result= (y[0]+y[1]+y[2])
print(result)