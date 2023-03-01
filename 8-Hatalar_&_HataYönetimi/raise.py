"""
x = 10

if x > 5:
    raise Exception("X 5 den büyük değer alamaz")
"""
"""
import re

def check_password(psw):
    if len(psw)<8:
        raise Exception("Parola en az 8 karakter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola kücük harf içermelidir ")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir ")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam harf içermelidir ")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alpha numeric karakter içermelidir ")
    elif re.search("s",psw):  #  backslash+s => boşluk 
        raise Exception("Parola boşluk içermemelidir")
    else:
        print("Geçerli parola")
    
password="12345678aA@ "

try:
    check_password(password)
except Exception as ex:
    print(ex)

"""
class Person:
    def __init__(self, name,year):
        if len(name)>10:
            raise Exception ("name alanı fazla karakter içeriyor")
        else:
            self.name=name

p= Person("Aliiiiiiiiiiiii",1989)