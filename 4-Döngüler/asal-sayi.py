"""
    Girilen bir sayının asal olup olmadığını bulun.
"""

sayi=int(input("Bir sayı giriniz: "))
asalmi= True 

if sayi>0:
    if sayi==1:
        asalmi= False

    for i in range(2,sayi):
        if (sayi & i==0):
            asalmi= False
            break

    if asalmi:
        print("Girilen sayı asaldır.")
    else:
        print("sayı asal değildir")
else:
    print("0 veya negatif bir sayının asallığı sorgulanamaz")