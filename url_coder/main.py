from urllib import request
import json

url = "https://jsonplaceholder.typicode.com/todos/"
data = request.urlopen(url).read().decode()

jsonData = json.loads(data)
print(jsonData[1].get('title'))


