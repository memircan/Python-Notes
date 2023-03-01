#def square(num): return num ** 2   

square = lambda num: num ** 2
numbers=[1,3,5,9,10,4]

#result=list(map(square, numbers))
#result=list(map(lambda num: num ** 2, numbers))   #üstteki ile aynı sonuc verir

#def check_even(num):
#    return num%2==0

check_even= lambda num: num%2==0

#result=list(filter(check_even,numbers))  #filter() fonksiyonu ise çağırılan fonksiyonun döndürdüğü değerin true olduğu durumlara göre liste döndürür.
#result=list(filter(lambda num: num%2==0,numbers)) #üsteki ile aynı sonuc
result=list(filter(lambda num: num%2==0,numbers))

print(result)