import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result=df
result=df.columns #datafram icinde bulunan kolonları getirir

result=df.head() # sayı girmezsek ilk 5 kayıt gelir
result=df.head(10) #ilk 10 kayıt

result=df.tail() # son 5 kayıt
result=df.tail(10) #son 10 kayıt

result = df["Column1"].head() #col1 ilk 5 kayıt
result = df.Column1.head()

result = df[["Column1","Column2"]].head() #col1 ve col2 ilk5 kaydı
result = df[5:15][["Column1","Column2"]].head() #5 ile 15 arasındaki kayıtlardan col1 ve col2 deki ilk5 kayıt

result = df >50 #50den büyükler icin true gelir
result =df[df >50] #50den büyükleri yazar, kücükleri NaN gösterir
result =df[df%2==0]

result=df["Column1"]>50  #col1 listelenir(50den büyükler)
result= df[df["Column1"]>50] #col1 in 50den büyük oldugu satırlar listeleni ama diger kolomlarda listelenir
result= df[df["Column1"]>50][["Column1","Column2"]] #üstekiyle aynı fakat fazladan sadece col2 gözükür
result= df[(df["Column2"]>50) & (df["Column1"]<=70)] #ve
result= df[(df["Column2"]>50) | (df["Column1"]<=70)] #veya

result=df.query("Column1 >=50 & Column1 % 2==0")


print(result)