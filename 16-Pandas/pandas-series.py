import pandas as pd
import numpy as np

#data
numbers= [20,30,40,50]
letters=["a","b","c","d",20]
scalar=5
dict={"a":10,"b":20,"c":30,"d":40}
random_numbers=np.random.randint(10,100,6)


#pandas_series = pd.Series(numbers) #indexleme 0 20  1 30  2 40  3 50
#pandas_series = pd.Series(letters)
#pandas_series=pd.Series(5,[0,1,2,3])
#pandas_series=pd.Series(numbers,["a","b","c","d"])
#pandas_series=pd.Series(dict)
#pandas_series=pd.Series(random_numbers)
pandas_series=pd.Series([20,30,40,50],["a","b","c","d"])

#result= pandas_series[0] #20
#result= pandas_series[:2]
#result=pandas_series.ndim #1 boyutlu
#result=pandas_series.shape 
#result=pandas_series.sum elemanları toplar
#result=pandas_series.max
#result=pandas_series.min
#result=pandas_series + pandas_series 
#result=pandas_series + 50 #her eleman üzerine +50
#result=np.sqrt(pandas_series)
#result=pandas_series >=50
#result=pandas_series % 2 ==0 #çift sayılar


#print(pandas_series)
#print(result)


opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total =opel2018 + opel2019

print(total["astra"])


