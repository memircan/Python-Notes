#name="Emircan Tamer"

"""
for letter in name:
    if letter=="a": 
        break     #a harfine gelince yazmayı durdurur
    print(letter)
"""

"""
for letter in name:
    if letter=="a": 
        continue   #a harfini atladı ekrana yazdırmadı
    print(letter)
"""


"""
x=0
while x<5:
    if x==2:
        break
    print(x)
    x+=1
"""
"""
x=0
while x < 5:
    x+=1
    if x==2:
        continue
    print(x)
"""

# 1-100 e kadar tek sayıların toplamı

x=0
toplam=0
while x<=100:
    x+=1
    if (x % 2==0):
        continue
    toplam=toplam+x

print(toplam)

    