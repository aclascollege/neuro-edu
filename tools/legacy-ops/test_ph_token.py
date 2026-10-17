import requests
import os

token = os.getenv("PRODUCTHUNT_TOKEN")
if not token:
    raise RuntimeError("Set PRODUCTHUNT_TOKEN before running this script.")
url = "https://api.producthunt.com/v2/api/graphql"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

query = """
{
  viewer {
    user {
      id
      name
      username
    }
  }
}
"""

response = requests.post(url, headers=headers, json={"query": query})
if response.status_code == 200:
    data = response.json()
    if 'data' in data and data['data']['viewer']:
        user = data['data']['viewer']['user']
        print(f"Connected successfully as: {user['name']} (@{user['username']})")
    else:
        print(f"Token verified but no user found: {data}")
else:
    print(f"Error: {response.status_code} - {response.text}")
