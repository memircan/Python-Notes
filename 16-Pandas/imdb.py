from unittest import result
import pandas as pd

df = pd.read_csv('16-Pandas\imdb.csv')



# 1- Dosyada Hakkındaki bilgiler
# 2- ilk5 kayıt
result=df.head()
# 3- ilk 10kayıt
result=df.head(10)
# 4- son 5 kayıt
result=df.tail()
# 5- son 10 kayıt
result=df.tail(10)
# 6- sadece Movie_Title kolonun alın
result=df["Movie_Title"]

# 7- sadece Movie_Title kolonun içeren ilk 5 kaydı alın 
result=df["Movie_Title"].head()

# 8- sadece Movie_Title ve rating kolonunu iceren ilk 5 kaydı
result=df[["Movie_Title","Rating"]].head()

# 9- sadece Movie_Title ve rating kolonunu iceren son7 kaydı
result=df[["Movie_Title","Rating"]].tail(7)

# 10- sadece movie title ve rating kolnunu iceren ikinci 5 kaydı alın 
result=df[5:10][["Movie_Title","Rating"]].head()

#11- sadece movie title ve rating kolonun iceren ve imdb puanı 8 ve üstünde olan kayıtlardan ilk 50 
result= df[df["Rating"]>=8.0] [["Movie_Title","Rating"]].head(50)

#12- yayın tarihi 2014-2015 arasında olan filmlerni isimlerini getiriniz
result= df[(df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)]["Movie_Title"]

#13- degerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8-9 arasında olanlar
result= df[ (df["Num_Reviews"]>=100000) | ( (df["Rating"]>=8) & (df["Rating"]<=9) )][["Movie_Title","Rating","Num_Reviews"]]


print(result)