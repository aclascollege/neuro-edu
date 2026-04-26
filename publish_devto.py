import requests
import json

api_key = "MCJzWCZDpiJTgi8EmYiwh1D1"
url = "https://dev.to/api/articles"

with open("devto_article.md", "r", encoding="utf-8") as f:
    body = f.read()

payload = {
    "article": {
        "title": "Building the First Anti-Fragile University: Introducing ACLAS Neuro-Edu SDK v3.0 🚀",
        "published": True,
        "body_markdown": body,
        "tags": ["ai", "opensource", "education", "python"],
        "main_image": "https://aclas.college/uploads/system/8b0b26b6b391297deb6e9b56768404f5.png"
    }
}

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Article published successfully!")
    print("URL:", response.json().get("url"))
else:
    print(f"Failed to publish article. Status code: {response.status_code}")
    print("Response:", response.text)
