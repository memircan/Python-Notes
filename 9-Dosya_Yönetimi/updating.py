# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20) #20. konumdan itibaren deneme yazar
#     file.write("deneme")  #r+ modu: dosyayı acma,okuma ve yazma modu


# with open("newfile.txt","r+",encoding="utf-8") as file:
#    print(file.read())

# ************ Sayfa sonunda güncelleme ************



#with open("newfile.txt","a",encoding="utf-8") as file:
#    file.write("\nEmircanTamer")

# *********** Sayfa başında güncelleme **********

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="efe turan\n" + content
#     file.seek(0)
#     file.write(content)
    
#with open("newfile.txt","r",encoding="utf-8") as file:
#    print(file.read())    

# ********* Sayfa ortasında güncelleme 


with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"yılmaz aygün\n")  #verdigimiz index numarasından önceki indexe ekler
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())