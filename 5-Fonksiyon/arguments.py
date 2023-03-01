"""
def changeName(n):
    n="emir"

name="mustafa"

changeName(name)
print(name)


def change(n):
    n[0]="istanbul"

sehirler=["ankara","izmir"]



change(sehirler[:]) #slicing işlemi


print(sehirler)


"""
#def add(a,b,c=0):
#    return sum((a,b,c))   # sum fonksiyonu lise içi toplamaya yarar
"""

def add(*params):          #parametreleri tektek yazmak yerine parametre isminden önce bir tane "*" 
    return sum((params))   # yazarak her seferinde üstteki gibi parametre eklememize gerek kalmıyor.
print(add(10,20))          # tuple tipi bir liste olmuş oluyor 
print(add(10,20,30))
print(add(10,20,30,45,50,65,20))
"""

def displayUser(**args):  #iki tane "**" yıldız yazarsak dictionary bilgi gelicegini söylemis olıruz
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name="Emir", age=19,city="Kocaeli")
displayUser(name="mustafa", age=15,city="istanbul",phone="12345")
displayUser(name="tamer", age=18,city="ankara",phone="12345",email="tamer@gmail.com")