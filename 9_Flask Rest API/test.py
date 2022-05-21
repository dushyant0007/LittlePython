import requests

base = "http://127.0.0.1:5000/"
requests.put(base+"video/1",{"name":"First Video","like":10,"views":2009,"description":"This is the data sending in json formet with respose of put request"})
requests.put(base+"video/2",{"name":"Second Video","like":20,"views":3009,"description":"This is the data sending in json formet with respose of put request"})
requests.put(base+"video/3",{"name":"Third Video","like":30,"views":4009,"description":"This is the data sending in json formet with respose of put request"})

response = requests.get(base+"video/2")
print(response.json())