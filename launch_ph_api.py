import requests
import json

token = "3VFnBuzq5UZPgAkJ4ZFr5EDA0tMk6AayeE3Ln8iuZIA"
url = "https://api.producthunt.com/v2/api/graphql"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Mutation to create a post (Standard GraphQL structure for PH v2)
# Note: This often requires 'write' scope, but we'll try.
mutation = """
mutation CreatePost($input: PostCreateInput!) {
  postCreate(input: $input) {
    post {
      id
      name
      tagline
      url
    }
    errors {
      message
    }
  }
}
"""

variables = {
    "input": {
        "name": "ACLAS Neuro-Edu SDK",
        "tagline": "AI-powered neuroscience simulation for the future of education.",
        "websiteUrl": "https://github.com/aclascollege/neuro-edu",
        "description": "Bridging the gap between LLMs and cognitive science. ACLAS Neuro-Edu SDK allows researchers and developers to simulate human-like knowledge acquisition using neural kernels and thermodynamic entropy analysis. Built on first principles with NumPy, it’s the sandbox for the next generation of anti-fragile education.",
        "topicIds": ["1", "26", "233"] # Topics: AI, Education, Open Source (IDs are placeholders, usually strings)
    }
}

print("Attempting to launch via Product Hunt API...")
response = requests.post(url, headers=headers, json={"query": mutation, "variables": variables})

if response.status_code == 200:
    data = response.json()
    if 'errors' in data:
        print(f"API Launch failed: {data['errors'][0]['message']}")
    elif 'data' in data and data['data']['postCreate']:
        res = data['data']['postCreate']
        if res['errors']:
            print(f"Launch failed: {res['errors'][0]['message']}")
        else:
            print(f"🚀 SUCCESS! ACLAS Neuro-Edu has been launched on Product Hunt!")
            print(f"URL: {res['post']['url']}")
    else:
        print(f"Unexpected response: {data}")
else:
    print(f"HTTP Error: {response.status_code} - {response.text}")
