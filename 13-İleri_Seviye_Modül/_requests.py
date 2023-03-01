import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos") #bilgi alma komutu .get
#result = result.text #bilgileri konsola yazdırma
result = json.loads(result.text)


for i in result:
    if i["userId"]==1:
        print(i["title"])




