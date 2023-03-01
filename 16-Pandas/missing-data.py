
from operator import index
from unittest import result
import pandas as pd
import numpy as np



data=np.random.randint(10,100,15).reshape(5,3)


df=pd.DataFrame(data, index=["a","c","e","f","h"],columns=["col1","col2","col3"])

df=df.reindex(["a","b","c","d","e","f","g","h"])

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["col4"]=newColumn


result=df
result=df.drop("col1",axis=1) # axis=1> kolon axis=0>satır col1 silinir
result=df.drop(["col1","col2"],axis=1)
result=df.drop("a",axis=0)
result=df.drop(["a","b","h"],axis=0) # a b h satırları silinir

result=df.isnull() #boş alanlar true gözükür
result=df.notnull()
result=df.isnull().sum() #kolonlarda ki toplam boş satır sayısını gösterir
result=df["col1"].isnull().sum() #sadece col1 deki boş satır sayısını gösterir
result=df[df["col1"].isnull()] 
result=df[df["col1"].isnull()]["col1"] 
result=df[df["col1"].notnull()]

result=df.dropna() #varsayılan axis=0 satırda NaN varsa o satır gelmez
result=df.dropna(axis=1)#sütünda nan varsa o sütün gelmez
result=df.dropna(how="any") #herhangi nan deger bulursa siler
result=df.dropna(how="all") #tüm satır nan oldugu durumda siler
result=df.dropna(subset=["col1","col2",],how="all") #öncelik olarak sadece col1 ve col2 yi inceler
result=df.dropna(subset=["col1","col2",],how="any")
result=df.dropna(thresh=2) #2 tane normal deger varsa bu durumda bu kayıtları silmez
result=df.dropna(thresh=3) # en az sayıda normal veri

result=df.fillna(value="no input") #nan verileri doldurur
result=df.fillna(value=1)

result=df.sum() #her kolondaki sayıların toplamı
result=df.sum().sum() #her şeyin toplamı
result=df.size #8x4 lük matris yani sonuc 32
result=df.isnull().sum().sum() #toplam boş alan sayısı



def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result=df.fillna(value = ortalama(df) )

print(result)
