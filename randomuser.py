import requests

url = "https://randomuser.me/api/"
data = requests.get(url).json()

user = data["results"][0]

print("Random User")
print("Name:", user["name"]["first"], user["name"]["last"])
print("Gender:", user["gender"])
print("Email:", user["email"])
print("Phone:", user["phone"])
print("Country:", user["location"]["country"])
print("City:", user["location"]["city"])
print("Username:", user["login"]["username"])
