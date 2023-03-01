import numpy as np
from numpy.core.fromnumeric import mean, reshape

#result = np.array([1,3,5,7,9])
#result = np.arange(1,10) #1dahil 10a kadar. 10dahil degil
#result = np.arange(10,100,3 ) #(Başlangıc , bitiş, artış miktarı)
#result = np.zeros(10) #10tane sıfır
#result = np.ones(10) 10tane 1
#result = np.linspace(0,100,5) #belli aralıkta eşit artısa sahip dizi - 0 25 50 75 100
#result = np.linspace(0,5,6) -0 1 2 3 4 5
#result = np.random.randint(0,10) #0dan 9a kadar birtane rastgele sayı üretir
#result = np.random.randint(20) #0dan 19a kadar sayı üretir .yani sadece üst sınır
#result = np.random.randint(1,10,3) #1 ile 10 arasında 3 sayı ürertir
#result = np.random.rand(5) #0 ile 1 arasında n tane sayı üretir
#result = np.random.randn(5) # eksi değerlerde katılmıs oldu
# np_array = np.arange(50)
# np_multi= np_array.reshape(5,10) 

# print(np_multi.sum(axis=1)) #satırların toplamı 
# print(np_multi.sum(axis=0)) #sütunların toplamı

rnd_numbers =np.random.randint(1,100,10)
print(rnd_numbers)

#result = rnd_numbers.max() #üretilen sayılardan en büyüğü
#result = rnd_numbers.min() # ""         ""        küçüğü
#result = rnd_numbers.mean() #sayıların ortalaması 
#result = rnd_numbers.argmax() #üretilen en büuyük sayının index numarası
result = rnd_numbers.argmin #           en kücük 


print(result)