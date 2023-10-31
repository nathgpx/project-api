import requests

url = "http://127.0.0.1:5000/songs"

r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    array = []
    for objeto in data:
        filtrado = {"track_name": objeto.get("track_name"),
                   "artist(s)_name": objeto.get("artist(s)_name") }
        array.append(filtrado)
    
    print(array)


else:
    print("Deu erro. Código de status:", r.status_code)





