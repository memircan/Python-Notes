from datetime import datetime,timedelta


#import datetime
simdi=datetime.now()
simdi=datetime.today() #now ile aynı

result= datetime.now() # çalıştığı anın zamanı
result= simdi.year
result= simdi.month
result= simdi.day
result= simdi.hour

result=datetime.ctime(simdi) #zamanla alakalı daha acıklayıcı bilgi verir
result=datetime.strftime(simdi,"%Y") #yıl bilgisi
result=datetime.strftime(simdi,"%X") #saat 
result=datetime.strftime(simdi,"%d") #gün
result=datetime.strftime(simdi,"%a") #gün bilgisi strign olarak yazar 
result=datetime.strftime(simdi,"%B") #ay -string
result=datetime.strftime(simdi,"%d %B %Y") #not: kücük harfler kısaltma, büyükük harf uzun
"""
t= "15 Nisan 2021"
gun, ay ,yıl = t.split()
print(gun)
print(ay)
print(yıl)
"""
t= "15 April 2021 hour 18:50:30"
result=datetime.strptime(t, "%d %B %Y hour %H:%M:%S") 
#result=result.year

birthday=datetime(2001,9,3,12,30,)

result=datetime.timestamp(birthday) #saniye cinsinden yazar
result=datetime.fromtimestamp(result) #saniye to datetime
result=datetime.fromtimestamp(0) #bilgisayarlar icin kullanılan milat bilgisi

result=simdi-birthday #timedelta 
#result= result.days
#result= result.seconds
#result= result.microseconds

result=simdi + timedelta(days=10) # kod calıstıgındaki gün bilgisine 10gün ekler
result=simdi - timedelta(days=10) 

print(result)