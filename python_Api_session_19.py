import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()

print("First 5 Post Titles:\n")

for post in posts[:5]:
    print(post["title"])




import json

restaurant = {
    "name": "Spice Villa",
    "location": "Ahmedabad",
    "cuisines": ["Indian", "Chinese", "Punjabi"],
    "rating": 4.6
}

json_data = json.dumps(restaurant, indent=4)

print(json_data)



import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My Playlist",
    "userId": 1,
    "body": "Python API Assignment"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())



import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2
}

response = requests.get(url, params=params)

posts = response.json()

print("Post IDs of userId = 2:\n")

for post in posts:
    print(post["id"])




import requests

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Authorization": "Bearer my_token_123"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)