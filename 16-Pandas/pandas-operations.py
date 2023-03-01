import pandas as pd
import numpy as np

data={
    "Col1":[1,2,3,4,5],
    "Col2":[10,20,13,20,25],
    "Col3":["abc","bcaa","ad","cba","dea"]
}

df=pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2=lambda x:x*x

result=df
result=df["Col2"].unique() #tekrarlayan degerleri getirmez
result=df["Col2"].nunique() #kactane tekil bilgi var onu gösterir
result=df["Col2"].value_counts()#her elemanın kactane tekrarladıgını gösterir

result=df["Col1"] * 2
result=df["Col1"].apply(kareal) #apple metoduna fonksiyon veriyoruz
result=df["Col1"].apply(kareal2) 
result=df["Col1"].apply(lambda x:x*x) 
result=df["Col3"].apply(len) 
df["Col4"]=df["Col3"].apply(len)
result=df.columns 
result=len(df.columns) #kolon sayısı

result=df.index #=> start=0, stop=5, step=1 

result=len(df.index) #satır sayısı
result=df.info #detaylı bilgileri verir

result=df.sort_values("Col2") #numerik sıralama, varsayılan: artan
result=df.sort_values("Col3") #alfabetik
result=df.sort_values("Col3",ascending=False) #azalan sıralama

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir"))




