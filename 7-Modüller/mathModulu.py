#Yöntem 1
#import math 
#import math as islem #kütüphaneye islem yazarak ulasabilirz

#value = dir(math)
#value = help(math)
#value = help(math.factorial)

# value=math.sqrt(49) #karekok alma
# value=math.factorial(5)
# value=math.floor(5.9) # aşağı yuvarlama 
# value=math.ceil(5.9) # yukarı yuvarlama 

#value=islem.factorial(5)



# Yöntem 2

#from math import * #bütün fonksiyonları import etmiş olduk math. yazmamıza gerek kalmıyor

#def sqrt(x):
#    print("x: "+ str(x))


from math import factorial,sqrt #bu şekilde sadece istedigimiz fonksiyonları getirmiş olruz

value=factorial(5)
value=sqrt(9)


print(value)