#for ve while döngüsüne alternatif olarak kullanılabilir
"""
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)


numbers= [x for x in range(10)]  #üstteki kod ile aynı işlevi yapıyor ama daha basit hali.
print(numbers)
"""
#####
"""
years=[1983,1999,2008,1956,1986]
ages= [2020-year for year in years]

print(ages)
"""
#####
"""
results=[x if x%2==0 else "TEK" for x in range(1,10)] 
print(results)
"""
#####

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

#####

numbers=[(x,y) for x in range(3) for y in range(3)]  #üstteki kodun basit hali
print(numbers)



