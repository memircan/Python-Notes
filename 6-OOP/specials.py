mylist=[1,2,3]
# myString="My String"

# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(self, title, director ,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi olusturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("film silindi")

m= Movie("Film adı","yönetmen adı",120)

print(str(mylist))
print(str(m))

print(len(mylist))
print(len(m))

del m

