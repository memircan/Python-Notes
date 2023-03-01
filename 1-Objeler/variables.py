maasAli = 5000
maasAhmet = 4000
vergi = 0.27


print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Değişken Tanımlama kuralları

# rakam ile başlayamaz 

number1=10
number1+=30
print(number1)

# Büyük küçük harf duyarlılığı 

age=20 
AGE=30
print(age)
print(AGE)

# Türkçe karakter kullanmayın

x=1              # int
y=2.5            # float
name="emir"      # string
isStudent = True # bool

# x,y,name, isStudent =(1, 2.5, "emir", True ) tek seferde değer atama şekli

a="10"
b="20"
print(a+b) # => 1020

firstname= "Emircan"
lastname=" Tamer"

print(firstname+lastname) # Emircan Tamer