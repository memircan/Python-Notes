# Inheritance (Kalıtım): Miras alma

#Person => name, lastname, age,eat(), run(), drink()
#student(Person) , Teacher(Person)    #Person'ın sahip oldugu özelliklere student sahip olmus oluyor


# Animal => Dog(Animal), Cat(Animal)


class Person():
    def __init__(self, fname,lname):
        self.firstName=fname
        self.lastName=lname
        print("Person created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")




class Student(Person):
    def __init__(self,fname,lname, number):
        Person.__init__(self,fname,lname)
        self.studentNumer=number
        print("Student created")

    # override
    def who_am_i(self):      #Aynı isimli metod, temel sınıftaki metodu ezer buna override denir
        print("I am a student") 

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)  #super metodu kullandıgımız zaman "self" yazmamıza gerek kalmıyor
        self.branch=branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1=Person("Ali","Yılmaz")
s1=Student("Çınar","Turan",1413)
t1=Teacher("Serkan","Yılmaz","Math")

print(p1.firstName +" "+p1.lastName)
print(s1.firstName +" "+s1.lastName+" "+ str(s1.studentNumer )) 

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()
p1.eat()
s1.eat()

