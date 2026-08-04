import requests

# ==========================================
# Task 1: Flipkart Orders Session
# ==========================================
print("--- Task 1: Flipkart Orders Session ---")
session = requests.Session()
url = "https://www.flipkart.com/account/orders"

response1 = session.get(url)
print("First Request Status:", response1.status_code)

response2 = session.get(url)
print("Second Request Status:", response2.status_code)

print("Cookies:", session.cookies.get_dict())
print()


# ==========================================
# Task 2: Weather API with Error Handling
# ==========================================
print("--- Task 2: Weather API ---")
# Replace with your actual OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q=Ahmedabad&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Current Temperature in Ahmedabad:", data["main"]["temp"], "°C")
else:
    print(f"Weather API Failed (Status {response.status_code}). Please replace 'YOUR_API_KEY' with your real API key.")
print()


# ==========================================
# Task 3: Async Fetch using HTTPX
# ==========================================
import asyncio
import httpx

async def fetch(client, url):
    response = await client.get(url)
    return response.json()

async def run_async_tasks():
    print("--- Task 3: Async Fetch using HTTPX ---")
    async with httpx.AsyncClient() as client:
        # Simulating concurrent requests using httpx (as required by task 3)
        url1 = "https://jsonplaceholder.typicode.com/posts/1"
        url2 = "https://jsonplaceholder.typicode.com/users/1"

        result1, result2 = await asyncio.gather(
            fetch(client, url1),
            fetch(client, url2)
        )

        print("Post 1 Title:", result1.get("title"))
        print("User 1 Name:", result2.get("name"))
    print()

asyncio.run(run_async_tasks())


# ==========================================
# Task 4: Bearer Token Auth
# ==========================================
print("--- Task 4: Bearer Token Auth ---")
def get_user_profile():
    url = "https://jsonplaceholder.typicode.com/users/1"
    headers = {
        "Authorization": "Bearer fake_token_123"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print("User Name:", data.get("name"))

get_user_profile()
print()


# ==========================================
# Task 5: OAuth 2.0 Redirect URL Generation
# ==========================================
print("--- Task 5: OAuth 2.0 Redirect URL ---")
import urllib.parse

def generate_spotify_oauth_url():
    client_id = "your_spotify_client_id"
    redirect_uri = "http://localhost:8080/callback"
    scopes = "user-read-private user-read-email"
    
    # Spotify authorization endpoint
    auth_url = "https://accounts.spotify.com/authorize"
    
    # Parameters for the authorization request
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scopes,
        "state": "random_secure_state_string"
    }
    
    # Generate urlencoded parameters and build the complete auth URL
    url_params = urllib.parse.urlencode(params)
    redirect_url = f"{auth_url}?{url_params}"
    return redirect_url

auth_url = generate_spotify_oauth_url()
print("Spotify OAuth Redirect URL:")
print(auth_url)
