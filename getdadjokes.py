import requests

url = "https://icanhazdadjoke.com/"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data["joke"])
else:
    print("Error:", response.status_code)
