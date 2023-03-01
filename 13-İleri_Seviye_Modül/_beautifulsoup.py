html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>tten</title>
</head>
<body> 
    <h1 id="Header">
        Python Kursu 
</h1>

    <div class="Grup1">
    <h2>Programlama</h2>

    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
    </div>  

    <div class="Grup2">
        <h2>Moduller</h2>
    
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
        </div>  

        <img src="" alt=""> 

</body>
</html>
"""





from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,"html.parser")

result= soup.prettify()  #dökümanı düzgün sekilde ekrana verir
result=soup.title 
result=soup.head
result=soup.body

result=soup.title.name 
result=soup.title.string #icerisindeki ifadeyi verir

result=soup.find_all("h2") #bütün h2 etiketlerini liste seklinde getirir
result=soup.find_all("h2")[0]
result=soup.find_all("h2")[1]

result=soup.div
result=soup.find_all("div")[1]
result=soup.find_all("div")[1].ul

result=soup.div.findChildren() #bütün alt elemanları getirir

result=soup.div.findNextSibling() #sonraki gruba gecis yaptık


print(result)