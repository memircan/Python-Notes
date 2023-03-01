import os  #genel olarak işletim sistemi ile alakalı bilgi sunar.
import datetime
#result= dir(os)
#result= os.name #işletim sistemi ismi

# dizin değiştirme
#os.chdir("C:\\")
#os.chdir("C:..") #bir üst klasöre gecer
#os.chdir("C:../..") #iki üste 
"""
"""

#  Klasör oluşturma
#os.mkdir("newdirectory") #dosya olusturur
#os.mkdirs("newdirectory\yeniklasör") #icice klasör olusruma 
#os.rename("newdirectory","yeniklasör") isim degisme
#os.rmdir("newdirectory") klasör silme
#os.removedirs("yeniklasör/yeniklasör") #alt dizindeki klasörüsilme


"""
"""
#result= os.getcwd() #etkin dizini ögrenme


#  Listeleme
#result=os.listdir() #dizindeki etkin klasörleri gösterir
#result=os.listdir("C:\\") #istedigimiz dizindeki klasörleri gösterir

#for dosya in os.listdir():
#    if dosya.endswith(".py"):
#        print(dosya)

"""
result= os.stat("os.py")  # stat metoduna bilgi sahini olmak istedigimiz dosya ismi girilir
result= result.st_size/1024
result=datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
result=datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
result=datetime.datetime.fromtimestamp(result.st_mtime) # degistirilme tarih
"""

#os.system("notepad.exe") #sistem üzerinden çalıştırma 


# path modülü --> uzantılar üzerindeki işlemler icin

result= os.path.abspath("_os.py") #istenilen dosyanın tam konumunu verir
result= os.path.dirname("C:/users/emircan/desktop/phton_deneme>") #tam konumu verilen dosyanın dizin ismi
result= os.path.exists("_os.py") #ismini verdigimiz dizin ya da dosyas ilgili konumda var mı
result=os.path.isdir("c:/users/emircan/desktop/phton_deneme/ModullerV2/") #klasörmü degilmi
result=os.path.isfile("c:/users/emircan/desktop/phton_deneme/ModullerV2/") #dosyamı degilmi


result=os.path.join("C:\\","deneme")
result=os.path.split("C:\\deneme")
result=os.path.splitext("_os.py") #dosyanın ismi ile uzantısını ayırır



print(result)