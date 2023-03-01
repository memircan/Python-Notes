from unittest import result
import pandas as pd

# customers={
#     "CustomerId":[1,2,3,4],
#     "FirstName":["Ahmet","Ali","Hasan","Canan"],
#     "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders={
#     "OrderId":[10,11,12,13],
#     "CustomerId":[1,2,5,7],
#     "OrderDate":["2020-07-04","2020-08-04","2020-07-07","2021-07-04"]

# }   

# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])


# print(df_customers)
# print(df_orders)



# result=pd.merge(df_customers,df_orders,how="inner") #merge=birleştirme ortak olanlar geldi
# result=pd.merge(df_customers,df_orders,how="left")
# result=pd.merge(df_customers,df_orders,how="right")
#result=pd.merge(df_customers,df_orders,how="outer")
customersA={
    "CustomerId":[1,2,3,4],
     "FirstName":["Ahmet","Ali","Hasan","Canan"],
     "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
 }

customersB={
    "CustomerId":[4,5,6,7],
     "FirstName":["Yagmur","Çınar","Cengiz","Can"],
     "LastName":["Bilge","Turan","Yılmaz","Top"]
 }

df_customersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result=pd.concat([df_customersA,df_customersB]) #varsayılan axis=0 alt alta toplama yapar
result=pd.concat([df_customersA,df_customersB],axis=1)#yan yana toplar 

print(result)


