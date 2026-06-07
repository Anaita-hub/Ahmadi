# ============================================================
# Advanced Lesson 5: Working with APIs (requests library)
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

# Install first: pip install requests
import requests
import json

# ============================================================
# PART 1: GET Request — Fetch Data from API
# ============================================================

# --- Simple GET request ---
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

print("Status code:", response.status_code)   # 200 = success

if response.status_code == 200:
    users = response.json()
    print(f"\nTotal users: {len(users)}")
    for user in users[:3]:   # Show first 3
        print(f"  {user['name']} | Email: {user['email']} | City: {user['address']['city']}")

# --- GET with parameters ---
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url, params=params)
posts = response.json()
print(f"\nPosts by user 1: {len(posts)}")
for post in posts[:2]:
    print(f"  Title: {post['title'][:50]}...")

# ============================================================
# PART 2: POST Request — Send Data to API
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    "title": "Learning Python APIs",
    "body": "APIs allow Python programs to communicate with web services.",
    "userId": 1
}

response = requests.post(url, json=new_post)
print("\nPOST response status:", response.status_code)
created = response.json()
print("Created post ID:", created["id"])
print("Title:", created["title"])

# ============================================================
# PART 3: Error Handling with APIs
# ============================================================

def safe_get(url, params=None):
    """Fetch data from URL safely with error handling."""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()   # Raises error for 4xx/5xx
        return response.json()
    except requests.exceptions.ConnectionError:
        print("ERROR: No internet connection.")
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ERROR: {e}")
    return None

data = safe_get("https://jsonplaceholder.typicode.com/todos/1")
if data:
    print(f"\nTodo: {data['title']} | Done: {data['completed']}")

# ============================================================
# PART 4: Headers & Authentication
# ============================================================

headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Example (won't run without real token — shows the pattern):
# response = requests.get("https://api.example.com/data", headers=headers)

print("\n--- Headers example ready (replace token for real API) ---")

# ============================================================
# PART 5: Free Weather API Example
# ============================================================

def get_weather(city):
    """Get weather for a city using Open-Meteo (no API key needed)."""
    # First get coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo = requests.get(geo_url, params={"name": city, "count": 1}).json()

    if not geo.get("results"):
        print(f"City '{city}' not found.")
        return

    location = geo["results"][0]
    lat, lon = location["latitude"], location["longitude"]

    # Then get weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather = requests.get(weather_url, params=params).json()
    current = weather["current_weather"]
    print(f"\nWeather in {city}:")
    print(f"  Temperature: {current['temperature']}°C")
    print(f"  Wind Speed:  {current['windspeed']} km/h")

get_weather("Kabul")

# ============================================================
# Practice Exercise:
# 1. Fetch all todos from jsonplaceholder and show only completed ones
# 2. Use the weather API to compare temperatures in 3 Afghan cities
# 3. Build a function that searches for a GitHub user and prints
#    their name, bio, and number of repositories
# ============================================================
