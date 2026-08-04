import requests


session = requests.Session()


session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
})


url = "https://www.flipkart.com/account/orders"


response1 = session.get(url)
print("First Request Status Code:", response1.status_code)


response2 = session.get(url)
print("Second Request Status Code:", response2.status_code)


print("\nSession Cookies:")
print(session.cookies)


print("\nSession Headers:")
print(session.headers)



import requests


url = "https://wttr.in/Ahmedabad"


params = {
    "format": "j1"  
}

try:
    
    response = requests.get(url, params=params)

    
    response.raise_for_status()

    
    data = response.json()

    
    temperature = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"Current temperature in Ahmedabad: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {description}")

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)

except requests.exceptions.RequestException as err:
    print("Request Error:", err)

except KeyError:
    print("Could not find temperature data.")






import asyncio
import httpx
async def fetch_trending_songs(client):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = await client.get(url)
    data = response.json()
    return f"Trending Song: {data['title']}"


async def fetch_trending_movies(client):
    url = "https://jsonplaceholder.typicode.com/posts/2"
    response = await client.get(url)
    data = response.json()
    return f"Trending Movie: {data['title']}"

async def main():
    async with httpx.AsyncClient() as client:
        
        songs, movies = await asyncio.gather(
            fetch_trending_songs(client),
            fetch_trending_movies(client)
        )

        print(songs)
        print(movies)

asyncio.run(main())



import requests

def get_user_profile():
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Fake Bearer token
    token = "fake_bearer_token_12345"

    # Authorization header
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse JSON response
        user = response.json()

        # Print user's name
        print("User Name:", user["name"])

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Call the function
get_user_profile()






import urllib.parse

# Spotify OAuth credentials
CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
REDIRECT_URI = "http://localhost:8000/callback"

# Permissions your app is requesting
SCOPE = "user-read-email user-read-private"

# Spotify OAuth authorization endpoint
AUTH_URL = "https://accounts.spotify.com/authorize"

# Query parametersA
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
}

# Generate the authorization URL
authorization_url = AUTH_URL + "?" + urllib.parse.urlencode(params)

print("Open this URL in your browser:")
print(authorization_url)