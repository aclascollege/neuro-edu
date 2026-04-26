import requests
import json

api_key = "MCJzWCZDpiJTgi8EmYiwh1D1"
url = "https://dev.to/api/comments"

payload = {
    "comment": {
        "body_markdown": "Hi DEV Community! 👋 We are **ACLAS College**, an institution dedicated to democratizing elite education through AI. We just joined and published our first post about our open-source **Neuro-Edu SDK** — a 3D cognitive simulation framework built with Python. We're excited to be here, learn from this amazing community, and share our journey in building an anti-fragile university. Looking forward to connecting with all the researchers, educators, and developers here! 🏛️🧠",
        "article_id": 3442016
    }
}

headers = {
    "Content-Type": "application/json",
    "api-key": api_key,
    "Accept": "application/vnd.forem.api-v1+json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Comment posted successfully!")
    print("Response JSON:", response.json())
else:
    print(f"Failed to post comment. Status code: {response.status_code}")
    print("Response:", response.text)
