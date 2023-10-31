import requests

url = "http://127.0.0.1:5000/songs"

dados ={
    "genre": "pop",
    
}

response = requests.put(url, json=dados)

response.text


if response.status_code == 200:
    print("Solicitação PUT bem-sucedida!")
   
    print("Resposta da API:", response.text)
else:
    print("Erro na solicitação PUT. Código de status:", response.status_code)

