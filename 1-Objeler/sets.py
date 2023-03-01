fruits = {'orange' ,  'apple', 'banana'}

#print(fruits[0]) indexlenemez , sıralanamaz

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple']) # listede daha önce olan elemanı eklemye calısırsak eklemicektir apple gibi.

fruits.remove('mango')
fruits.discard('apple')

#fruits.pop()  # normal listelerde son elemanı siler fakat sets listelerde rastgele bir şeyi siler

print(fruits)

# myList= [1,2,5,4,4,2,1]

# print(set(myList))
