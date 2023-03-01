import pandas as pd
from pandas.core.frame import DataFrame


list=[["Ahmet",50],["Ali",60],["can",70],["emir",80]]
dict={"Name": ["Ahmet","Ali","can","emir"],"Grade":[50,60,70,80]}
dict_list= [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"can","Grade":70},
                {"Name":"emir","Grade":80}
            ]

#df=pd.DataFrame()
#df=pd.DataFrame([1,2,3,4])

#df=pd.DataFrame(list,columns=["name","grade"], index=[1,2,3,4],dtype=float)
#df=pd.DataFrame(dict)
#df=pd.DataFrame(dict, index=["212","232","236","456"])
df=pd.DataFrame(dict_list)


print(df)



# s1= pd.Series([3,2,0,1])
# s2= pd.Series([0,3,7,2])


# data = dict(apples=s1, oranges = s2)

# df=pd.DataFrame(data)

# print(df)
