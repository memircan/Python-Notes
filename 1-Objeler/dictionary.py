# key - value

# 41 =>kocaeli 34=>istanbul

# city=["kocaeli","istanbul"]
# plate=[41,34]

# print(plate[city.index("kocaeli")])

#print(plate["kocaeli"]) =>41 amacımız bu sekilde key-value şekline yazdırmak

# plate= {"kocaeli" : 41, "istanbul":34}
# print(plate["kocaeli"])

# plate["ankara"]= 6
# print(plate)

from datetime import date, datetime


users = {  
"emircantamer" : {
    "age": datetime.now().year - 2001,
    "roles": ["admin","user"], 
    "email": "e.tamer@gmail.com" ,  
    "adress": "kocaeli" },

"mustafa": {
    "age": datetime.now().year - 2000,
    "roles": ["user"] ,
    "email": "musti@gmail.com" , 
    "adres": "kocaeli" }
}

print(users["emircantamer"]["age"])
