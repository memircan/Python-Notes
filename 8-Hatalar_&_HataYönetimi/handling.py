#error handling => hata yönetimi
'''
try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)  
except ZeroDivisionError:
    print("y için 0 girilemez")
except ValueError:
    print("x ve y için sayısal değer giriniz")
'''
# VEYA
"""
try:
    x=int(input("x: "))      #hataları tek satırda yazıp genel bir hata mesajı yazdırabiliriz
    y=int(input("y: "))
    print(x/y)  
except (ZeroDivisionError,ValueError) as e:  # sonuna "as e" şeklinde yazarak hangi hata oldgunu ekledik
    print("Yanlış bilgi girdiniz")
    print(e)   
"""
"""
try:
    x=int(input("x: "))      #hataları yazmadan genel bi hata alınca uyarı yazdırılır
    y=int(input("y: "))      # nerde hata oldgunu göremeyiz 
    print(x/y)  
except:  
    print("Yanlış bilgi girdiniz")
"""

while True:
    try:
        x=int(input("x: "))      # Kullanıcı hatalı veri girerse hata verip tekrar veri girmesini ister
        y=int(input("y: "))      
        print(x/y)  
    except Exception as ex:    #Exception =genel bir hata ,diğer hataları kaplar
        print("Yanlış bilgi girdiniz",ex) #yani kullanıcıya hangi hata oldugunu söylemiş oluruz
    else:
        break
    finally:
        print("try except sonlandı")


