import requests 
import json


with open('validation_x.json') as f:
    data = json.load(f)
    
    
url = 'http://127.0.0.1:8080/predict'
#r = requests.post(url,json={'V230':1.0,"C14":1.0,"V202":0.000000,"C8":1.0, "D1":0.0})
r = requests.post(url, json=data)
print(r.json())    