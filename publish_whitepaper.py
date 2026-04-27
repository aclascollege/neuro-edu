import requests

api_key = "MCJzWCZDpiJTgi8EmYiwh1D1"
url = "https://dev.to/api/articles"

with open("whitepaper_article.md", "r", encoding="utf-8") as f:
    body = f.read()

payload = {
    "article": {
        "title": "Deep Dive: The Cognitive Science Behind the ACLAS Neuro-Edu SDK 🏛️🧠",
        "published": True,
        "body_markdown": body,
        "tags": ["ai", "machinelearning", "education", "opensource"],
        "main_image": "https://aclascollege.github.io/neuro-edu/assets/dashboard_hero.png"
    }
}

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 201:
    print("Whitepaper article published successfully!")
    print("URL:", response.json().get("url"))
else:
    print(f"Failed to publish article. Status code: {response.status_code}")
    print("Response:", response.text)
