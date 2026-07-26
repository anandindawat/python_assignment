import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("First Post Title:", data[0]["title"])




import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First Post",
    "body": "Hello from Python!",
    "userId": 101
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())




import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

print("Usernames with .org email:\n")

for user in users:
    if user["email"].endswith(".org"):
        print(user["username"])




import requests

url = "https://www.omdbapi.com/"

params = {
    "apikey": "942ab187",
    "s": "Avengers"
}

response = requests.get(url, params=params)

data = response.json()

if data["Response"] == "True":
    print("Total Results:", data["totalResults"])
else:
    print("Error:", data["Error"])