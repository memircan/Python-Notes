#diğer operaatörler

# x = y = [1,2,3]
# z= [1,2,3]

# print(x==y)  # true  listedeki değerleri karsılastırıyor
# print(x==z) #true 

# print(x is y) # adres karşılaştırması cevap true 
# print(x is z) #false


x = [1,2,3]
y= [2,4]
del x[2]
y[1]=1
y.reverse()

print(x==y) # true
print(x is y)  #false 
print(x is not y) #true

# Membership operator : İn

x=["apple","banana"]
print("banana"in x)