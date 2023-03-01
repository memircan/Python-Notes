import numpy as np
import pandas as pd

personeller={
        "Çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
        "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
        "Yaş":[30,25,45,50,23,34,42],
        "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
        "Maaş":[5000,3000,4000,3500,2750,6500,4500]
}


 
df=pd.DataFrame(personeller)
result=df
result=df["Maaş"].sum() #bütün maaşlar toplamı
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups




#for name, group in df.groupby("Semt"):
 #    print(name)
 #    print(group)


# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result=df.groupby("Semt").get_group("Kadıköy") #kadıköyle oturan kisileri getirir
result=df.groupby("Departman").get_group("Muhasebe")

result=df.groupby("Departman").mean() #departmanların yaş ve maaş ortalaması
result=df.groupby("Departman")["Maaş"].mean() #sadece maas ortalaması

result=df.groupby("Semt")["Yaş"].mean() #semtlerin yaş ortalaması
result=df.groupby("Semt")["Çalışan"].count() #semtlere göre calısan sayısı

result=df.groupby("Departman")["Yaş"].max() #departmandaki max yaş
result=df.groupby("Departman")["Maaş"].max()
result=df.groupby("Departman")["Maaş"].max()["Muhasebe"] #tüm departmanlar icinden muhasebenin max maaşı
result=df.groupby("Departman").agg(np.mean) #departmana göre ortalama hesaplama (yaş ve maas ort)
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max]) #hesaplamayı tek bir işlemde yapmamızı saglar
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max]).loc["Muhasebe"] #sadece muhasebe icin hesaplar
print(result) 