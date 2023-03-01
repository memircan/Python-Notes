with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0)  #imleci, parantezin icinde yazılı olan konuma gönderir
    print(file.tell())  #tell fonksiyonu o anki imlecin konumunu verir
    content2 = file.read(10)
    print(content2)


