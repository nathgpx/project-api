import requests 

url = "http://127.0.0.1:5000/songs"

response = requests.get(url)

if response.status_code == 200:
    data= response.json()
    print(data)
else:
    print( "Deu merda", response.status_code)
    