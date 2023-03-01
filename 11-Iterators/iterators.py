#                                 iterator=yineleyici
# liste =[1,2,3,4,5]

# iterator= iter(liste)

# print(next(iterator)) #iterator'u next metodu ile her cagırdıgımızda listenin bir elemanı yazdırılır -1
# print(next(iterator)) # 2 yazar
# print(next(iterator)) # 3 yazar
# print(next(iterator))
# print(next(iterator))



# liste =[1,2,3,4,5]
# iterator=iter(liste)

# while True:
#     try:
#         element=next(iterator)    #for döngüsünün arka planda yaptıgı işlem
#         print(element)
#     except StopIteration:
#         break



class MyNumbers:
    def __init__(self, start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<= self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration

list=MyNumbers(10,20)

for x in list:
    print(x)




