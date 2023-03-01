'''
class Person:
    # class attributes
    address = "no information"

    #constructor (yapıcı metod)
    def __init__(self ,name,year):
        # object attributes
        self.name= name
        self.year= year
        

    # instance methods (örnekmethods)
    def intro(self):
        print("Hello There "+ self.name)

    def calculateAge(self):
        return 2021 - self.year

#object (instance)

p1 = Person(name='ali',year=1990)
p2 = Person("emir",2001)

p1.intro()
p2.intro()
print(f"adım {p1.name} ve yaşım {p1.calculateAge()}")
print(f"adım {p2.name} ve yaşım {p2.calculateAge()}")

#updating
p1.name="ahmet"
p2.address="kocaeli"


# accesing object attributes
#print(f'p1 name:{p1.name} year: {p1.year} address:{p1.address}')
#print(f'p2 name:{p2.name} year: {p2.year} address:{p2.address}')
'''

class Circle:
    #Class object attribute
    pi=3.14

    def __init__(self, yaricap=1):
        self.yaricap=yaricap
        
    #Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() #yaricap=1
c2 = Circle(5)

print(f' c1: alan= {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()} ' )
print(f' c2: alan= {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()} ' )