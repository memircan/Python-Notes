from unittest import result
import pandas as pd


df = pd.read_csv('16-Pandas/nba.csv')


# 1- ilk 10 kaydı getiriniz.
result=df.head(10)

# 2- Toplam kaç kayıt vardır
result=len(df.index)

# 3- tün oyuncuların toplam maaş ortalaması nedir?
result=df["Salary"].mean()

# 4- en yüksek maaş
result=df["Salary"].max()

# 5- en yüksek maası alan oyuncu kimdir?
result=df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]

# 6- yaşı 20-25 arasında olan oyuncuların isim ve oyndakıkları takımları 
result=df[ (df["Age"]>=20) & (df["Age"]<=25)][["Name","Team"]]

# 7- "John Holland" isimli oyuncunun oynadıgı takım hangisidir.
result=df[df["Name"]=="John Holland"][["Name","Team"]]

# 8- takımlara göre oyuncularım ortalama maaş bilgisi
result=df.groupby("Team").mean()["Salary"]


# 9- kac farklı takım mevcut
result=len(df["Team"].unique())
result=df["Team"].nunique() 
result=len(df.groupby("Team"))


#10- her takımda kac oyuncu oynamakta
result=df["Team"].value_counts()

#11- ismi icinde "and" gecen kayıtları bulunuz

df.dropna(inplace=True)
# 1.yol
result=df[df["Name"].str.contains("and")]

# 2.yol
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result=df[df["Name"].apply(str_find)]

print(result)