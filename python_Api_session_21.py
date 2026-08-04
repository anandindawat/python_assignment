import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First Post",
    "body": "Hello API",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())



import requests

url = "https://jsonplaceholder.typicode.com/posts"

playlist_name = input("Enter Playlist Name: ")
description = input("Enter Playlist Description: ")

data = {
    "title": playlist_name,
    "body": description,
    "userId": 1
}

response = requests.post(url, json=data)

result = response.json()

print("Playlist Created Successfully")
print("Playlist ID:", result["id"])


