"""# Python Requests Library & API – Detailed Explanation

Your code demonstrates how to interact with APIs using Python's **requests** module. Let's understand each topic in detail.

---

# 1. API (Application Programming Interface)

An **API** is a set of rules that allows different software applications to communicate with each other.

### Real-Life Example

Imagine you are in a restaurant:

* **Customer** → Your Python Program
* **Waiter** → API
* **Kitchen** → Server/Database

You tell the waiter what you want. The waiter sends your request to the kitchen and brings back the response.

Similarly:

```
Python Program → API → Server
```

### Why APIs are Used?

* Access online data
* Connect applications
* Automate tasks
* Build web/mobile applications

### Example APIs

* Weather API
* Google Maps API
* Facebook API
* OpenAI API
* JSONPlaceholder API (used in your code)

---

# 2. HTTP Methods

HTTP methods define what action you want to perform on the server.

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Retrieve data         |
| POST   | Create new data       |
| PUT    | Update existing data  |
| PATCH  | Partially update data |
| DELETE | Delete data           |

---
"""
# 3. GET Request

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

# GET is used to fetch data from a server.

### What happens?

# 1. Request sent to server
# 2. Server processes request
# 3. Server returns data

### Response Object

print(response.status_code)

# Shows status code.
# Example:
#     200
# Meaning request was successful.


### JSON Data
print(response.json())
# Converts JSON response into Python objects.
"""
Server returns:

{
   "id": 1,
   "title": "sample title"
}"""

# Python converts to:

{
   "id":1,
   "title":"sample title"
}

### URL

print(response.url)

# Displays final URL.

# Output:

# https://jsonplaceholder.typicode.com/posts

### dir()

print(dir(response))

# Shows all available methods and attributes of response object.
"""
# Examples:

response.status_code
response.json()
response.headers
response.text
response.url
"""
# 4. Query Parameters

params = {
    "userId":1
}

Used to filter data.

```python
response = requests.get(
    url,
    params=params
)
```

Actual URL becomes:

```text
https://jsonplaceholder.typicode.com/posts?userId=1
```

### Why use Parameters?

Suppose database has 1000 posts.

Without parameter:

```python
GET /posts
```

Returns all posts.

With parameter:

```python
GET /posts?userId=1
```

Returns only posts of user 1.

---

# 5. Sending Headers

Headers provide extra information to the server.

```python
headers = {
    "User-Agent":"MyApp"
}
```

Request:

```python
requests.get(
    url,
    headers=headers
)
```

### Common Headers

```python
headers = {
    "User-Agent":"MyApp",
    "Accept":"application/json",
    "Authorization":"Bearer token"
}
```

### Why Headers?

* Authentication
* Identify application
* Specify content type
* Security

---

# 6. POST Request

Used to create new resources.

```python
data = {
    "title":"Python API",
    "body":"Learning requests module",
    "userID":1
}
```

```python
response = requests.post(
    url,
    json=data
)
```

### What happens?

Before:

```
Database
---------
Post 1
Post 2
```

After POST:

```
Database
---------
Post 1
Post 2
Post 3
```

### Response

```python
{
 "id":101,
 "title":"Python API"
}
```

Server creates new record.

---

# 7. PUT Request

Used to update an entire resource.

```python
response = requests.put(
    url,
    json=update_data
)
```

### Before

```json
{
 "id":1,
 "title":"Old Title"
}
```

### After

```json
{
 "id":1,
 "title":"Python API"
}
```

Entire record gets replaced.

---

## Difference Between PUT and PATCH

### PUT

Updates complete resource.

```python
{
 "name":"Ram",
 "age":20
}
```

### PATCH

Updates only specific fields.

```python
{
 "age":21
}
```

---

# 8. DELETE Request

Used to remove data.

```python
response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)
```

### Before

```
Post 1
Post 2
Post 3
```

### After

```
Post 2
Post 3
```

---

# 9. Status Codes

HTTP status codes indicate request result.

## Success Codes

| Code | Meaning    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

---

## Client Errors

| Code | Meaning      |
| ---- | ------------ |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |

---

## Server Errors

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |

---

# 10. API Authentication

Many APIs require authentication.

### API Key Example

```python
headers = {
    "API-Key":"abcd1234"
}
```

---

### Bearer Token Example

```python
headers = {
    "Authorization":"Bearer xyz123"
}
```

Used by:

* OpenAI API
* GitHub API
* Google APIs

---

# 11. Error Handling

Network problems can occur.

Without error handling:

```python
response = requests.get(url)
```

Program may crash.

---

### Using Try Except

```python
try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(e)
```

---

### raise_for_status()

Checks status code.

If:

```python
404
500
401
```

Exception is raised automatically.

---

### Common Exceptions

```python
ConnectionError
Timeout
HTTPError
RequestException
```

Example:

```python
try:
    requests.get(url, timeout=5)

except requests.Timeout:
    print("Request timed out")
```

---

# 12. Working with Sessions

Session maintains settings across requests.

```python
session = requests.Session()
```

### Set Headers Once

```python
session.headers.update({
    "User-Agent":"MyApp"
})
```

Now every request uses that header.

```python
session.get(url1)
session.get(url2)
session.get(url3)
```

---

### Benefits

✅ Faster

✅ Reuses connection

✅ Maintains cookies

✅ Useful for login systems

---

# 13. Pagination

Used when API contains large amounts of data.

Instead of returning:

```python
10000 records
```

API returns small chunks.

---

### Example

```python
params = {
    "_page":3,
    "_limit":5
}
```

Meaning:

```text
Page Number = 3
Records Per Page = 5
```

---

### Data Distribution

Page 1:

```
1-5
```

Page 2:

```
6-10
```

Page 3:

```
11-15
```

Only records 11-15 are returned.

---

# Complete Requests Workflow

```text
1. Create Request
        ↓
2. Add Parameters
        ↓
3. Add Headers
        ↓
4. Send Request
        ↓
5. Receive Response
        ↓
6. Check Status Code
        ↓
7. Convert JSON
        ↓
8. Handle Errors
        ↓
9. Process Data
```

# # Interview Questions

# ### Q1. What is an API?

# An API is a mechanism that allows two software applications to communicate with each other.

# ### Q2. Difference between GET and POST?

# | GET               | POST                |
# | ----------------- | ------------------- |
# | Retrieve data     | Create data         |
# | Parameters in URL | Data in body        |
# | Safe              | Changes server data |

# ### Q3. What is JSON?

# JSON (JavaScript Object Notation) is a lightweight format used for data exchange between client and server.

# ### Q4. Why use Sessions?

# Sessions improve performance by reusing connections and maintaining cookies.

# ### Q5. What is Pagination?

# Pagination divides large datasets into smaller pages to improve performance and reduce bandwidth usage.

# These concepts form the foundation of working with REST APIs in Python and are very important for Data Science, Backend Development, Flask, Django, and Software Engineering interviews.
