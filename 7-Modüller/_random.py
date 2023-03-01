import random

#result= dir(random)
#result= help(random)

result=random.random() #0.0 - 1.0 arasında
result=random.uniform(1,10) # 1 ile 10 arası float
result=random.randint(1,100) # 1ile 100 arası int

names= ["ali","yağmur","emir","ahmet"]
result=names[random.randint(0,len(names)-1)]
greeting= "hello there"

result=random.choice(names)
result=random.choice(greeting)

liste=list(range(10)) #sıralı
random.shuffle(liste) #liste elemanlarını karıstırdı

liste = range(100)
result=random.sample(liste,3) #liste içinden rastgele 3 sayı getirir

result=random.sample(names,2)



print(result)