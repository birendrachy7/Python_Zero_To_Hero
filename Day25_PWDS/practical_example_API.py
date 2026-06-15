import requests


response = requests.get(
    "https://randomuser.me/api"
)

user = response.json()
print(user)

print("=="*40) 

print(user['results'][0]["name"])