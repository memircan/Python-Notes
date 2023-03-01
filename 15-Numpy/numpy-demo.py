import numpy as np

# 1- (10,15,30,45,60) ddeğerlerine sahip numpy dizisi olusturun.
"""
numbers=np.array([10,15,30,45,60])
print(numbers)
"""
# 2- (5-15) arasındaki sayılarla numpy dizisi olusturn
"""
numbers=np.arange(5,15)
print(numbers)
"""
# 3- (50-100) arasında 5er5er artan dizi oluıstur
numbers=np.arange(50,100,5)

# 4- 10 elemanlı sıfırlşardan olusan dizi
numbers=np.zeros(10)

# 5- 10elemanlı birlerden olusan dizi
numbers=np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin
numbers=np.linspace(0,100,5)

# 7- (10-30) arasından rastgele 5tamsayı üretin
numbers=np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin
numbers=np.random.randn(10)


# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris olustur.
"""
numbers=np.random.randint(10,50,15).reshape(3,5)
"""



# 10- üretilen matrisin satır ve sütıun sayılarının toplamını hesaplayın
""""
matris=numbers=np.random.randint(10,50,15).reshape(3,5)
rowTotal=matris.sum(axis=1) #satır
colTotal=matris.sum(axis=0) #sutun

print(matris)
print(f"{rowTotal} <-sütün toplamı")
print(f"{colTotal} <-kolon toplamı")
"""
# 11- üretilen matrisin en büyük , en kücük ve ortalaması nedir
"""
result=matris.max()
result=matris.min()
result=matris.mean()
"""

# 12- üretilen matrisin en büyük değerinin indexi kactır
"""
result=matris.argmax()
result=matris.argmin()
"""


# 13- (10-20 ) arasındaki sayıları iceren dizinin ilk 3 elemanını secin
"""
arr=np.arange(10,20)
print(arr)

result=arr[:3]
"""


#14- üretilen dizinin elemanlarını tersten yazdır.
"""
result=arr[::-1]
"""
#15- üretilen matrisin ilk satırını yazdırın
"""
matris=numbers=np.random.randint(10,50,15).reshape(3,5)

result=matris[0]
"""
#16-matrisin 2.satıor 3.sutundaki elemanı haNGİİS
"""
print(matris)
result=matris[1,2]
"""
#17- matrisin tüm satırlardsaki ilk elemanını secin
"""
result=matris[:,0]
"""
#18-matrisin her bir elemanını karesini alınız
"""
result=matris**2
"""
#19-üretilen matrisin elemanlaırın hangisi pozitif cift sayıdır. aralık(-50, +50)
matris=numbers=np.random.randint(-50,50,15).reshape(3,5)
print(matris)

ciftler=matris[matris%2==0]
result=ciftler[ciftler>0]


print(result)