import numpy as np

numbers=np.array([0,5,10,15,20,25,50,75])

result=numbers[5]
result=numbers[-1] #son deger
result=numbers[0:3] #0 ile 3 arasında 3dahil degil
result=numbers[:3] # üstekiyle aynı
result=numbers[3:] #3den sona kadar 
result=numbers[::] #bütün listeyi temsil eder
result=numbers[::-1] #tersten yazdırır

numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]]) # 3e3lük matris

result=numbers2[0] # 0 5 10
result=numbers2[2] # 50 75 85
result=numbers2[0,2] # 10
result=numbers2[2,1] #75

result=numbers2[:,2] # ":" tüm satırları seçer, 2 yazdıgımızda her satırdan 2. elemanı alır 
                     # 10 25 85 
result=numbers2[:,0] # 0 15 50

result=numbers2[:,0:2] # tüm satırların icerisinden 0 ile 2. index arasındakileri alır 2haric                 
                       # [0 5] [15 20] [50 75]
 
result=numbers2[-1,:]  #50 75 85 

result=numbers2[:2,:2] # ilk 2 satırdan ilk2 kolon 0 5 - 15 20 

arr1=np.arange(0,10)
#arr2=arr1 # referans - referans aldıgında biri degisirse digeride degisir 
                        #degisiklik adres üzerinde gerceklesir 
arr2= arr1.copy()  #bu şekilde ikisi icinde farklı adresler olusur
                   #bir listede yaptıgımız degisiklik digerinde etki etmez


arr2[0]=20

print(arr1)
print(arr2)

#print(result)