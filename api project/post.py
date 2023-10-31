import requests 

url = "http://127.0.0.1:5000/songs"

data = {
    "genre": "pop",
    "musica": "cherry"
}

response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

if response.status_code == 200:
    data = response.json()
    print(data)
    print(response.status_code)
else:
    print("Deu erro. Código de status:", response.status_code)