import requests
 
response = requests.get("https://randomuser.me/api/")
user = response.json()
# print(user)
name = user["results"][0]["name"]["first"]
age = user["results"][0]["dob"]["age"]
gender =user["results"][0]["gender"]
email = user["results"][0]["email"]
last_name = user["results"][0]["name"]["last"]


 
print("First Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Email:", email)
print("Last Name:", last_name)
