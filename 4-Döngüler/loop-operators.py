# Range Metodu
"""
for item in range(10):  #0dan 9a kadar yazdı. (2,10) seklinde yazarsak 2den 9a kadar yazar
    print(item)         # (50,100,10) seklinde yazarsak 50den baslayıp 100e kadar 10fark ile yazdı


print(list(range(50,100,20)))  #liste şeklinde yazdı
"""

# enumerate metodu
"""
greeting="Hello"
index=0

for index,letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")

"""

# zip metodu

list1=[1,2,3,4,5]                       
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1, list2, list3)))   

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)

