from dataclasses import dataclass
import pandas as pd

data=pd.read_csv("16-Pandas/nba.csv")

data.dropna(inplace=True) #orijinal data üzerinde degisiklilk yapar


#data["Name"]= data["Name"].str.upper()             #data icindeki name kolonundaki bütün harfleri büyük yapar
#data["Name"]= data["Name"].str.lower()

#data["index"]=data["Name"].str.find("a")           #name icinde buldugu "a" harfinin index numarasını yazar

#data=data.Name.str.contains("Jordan")              #jordan kelimesini bulup true yazar
#data=data[data.Name.str.contains("Jordan")]        #data icine yollarsak ismi jordan olan oyuncuları getirir
#data=data.Team.str.replace(" ","-") boşluklara - ekler

data[["FirstName","LastName"]]=data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
#data icine 2 tane kolon olusturduk. name kolonu icinden

print(data.head())