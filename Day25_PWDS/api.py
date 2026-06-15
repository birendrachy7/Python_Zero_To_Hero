# 1. API (API)

# 2. HTTPS Methods


import requests


response  = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())
print(dir(response))
print(response.url)
print()


print('*'*40)


#4. 

params={
    "userId": 1
}

response= requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params= params
)

print(response.json()[:3])

print("*"*40)
print("Sending Header")

print("*"*40)
# 5. Sending Header
headers = {
    "User-Agent": "MyApp"
}
response= requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    headers = headers
)

print(response.status_code)


#6. POST Request

print("*"*40)
print("Post Request")

print("*"*40)
data={
    "title":"Python API",
    "body":"Learning requests module",
    "userID": 1
    
}

response= requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json = data
)

print(response.json())

# 7. PUT request
print("*"*40)
print("PUT Request")

print("*"*40)

update_data={
    "id":1,
    "title":"Python API",
    "body":"Learning requests module",
    "userID": 1
    
}

response= requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json = update_data
)

print(response.json())



print("*"*40)
print("Delete Request")

print("*"*40)


response= requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code)



#9. Status Code

# 200 - success
# 201 - Resource created
# 400 - Bad request
# 401 - unauthorized
# 404 - not found
# 500 - internal server error



print("*"*40)
print("API aUTHENTICATION")

print("*"*40)
#10. API Authentication



print("*"*40)
print("Error Handling")
# 11. Error HAndling
print("*"*40)

try:
    response= requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )
    response.raise_for_status()
    print("Success")

except requests.exceptions.RequestException as e:
    print(e)
    
    
    
# 12. Working with sessions
# session = requests.Session()

# session.headers.update({
    
#     "User-Agent":"MyApp"
# })


print("*"*40)
print("Pagination")

print("*"*40)
# 13. Pagination

params={
    "_page":3,
    "_limit":5
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)
print(response.json())