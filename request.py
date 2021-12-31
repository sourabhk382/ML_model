
import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Temperature':30, 'Humidity':0.8, 'Windspeed':40})

print(r.json())
