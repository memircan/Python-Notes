#Bankamatik Uygulaması

EmirHesap ={
    "ad":"Emircan Tamer",
    "hesapNo":"132456",
    "bakiye":3000,
    "ekHesap":2000
}

ErenHesap ={
    "ad":"Eren Tıtın",
    "hesapNo":"123456",
    "bakiye":2000,
    "ekHesap":1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap["bakiye"]>= miktar):
        hesap["bakiye"] -=miktar
        print("paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye'] + hesap["ekHesap"]

        if (toplam>=miktar):
            ekhHesapKullanimi = input("Ek hesap kullanılsınmı? (e/h)")
            if ekhHesapKullanimi=="e":
                ekHesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("paranızı alabiliriniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır ")
        else:
            print("üzgünüz bakiyeniz yetersiz.")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır. Ek hesap limitiniz ise {hesap["ekHesap"]} TL bulunmaktadır. ')



paraCek(EmirHesap,3000)


print('************')

paraCek(EmirHesap,2000)



