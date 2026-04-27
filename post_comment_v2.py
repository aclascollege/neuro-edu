import requests

api_key = "MCJzWCZDpiJTgi8EmYiwh1D1"
url = "https://dev.to/api/comments"

msg = "Hi DEV Community! 👋 We are **ACLAS College**, an institution dedicated to democratizing elite education through AI. We just joined and published our first post about our open-source **Neuro-Edu SDK** — a 3D cognitive simulation framework built with Python. We're excited to be here, learn from this amazing community, and share our journey in building an anti-fragile university. Looking forward to connecting with all the researchers, educators, and developers here! 🏛️🧠"

# Variation 1: article_id as int
payload1 = {
    "comment": {
        "body_markdown": msg,
        "article_id": 3442016
    }
}

# Variation 2: article_id as string
payload2 = {
    "comment": {
        "body_markdown": msg,
        "article_id": "3442016"
    }
}

headers = {
    "Content-Type": "application/json",
    "api-key": api_key,
    "Accept": "application/vnd.forem.api-v1+json"
}

print("Trying Variation 1...")
r1 = requests.post(url, headers=headers, json=payload1)
print(f"Status: {r1.status_code}")

if r1.status_code != 201:
    print("Trying Variation 2...")
    r2 = requests.post(url, headers=headers, json=payload2)
    print(f"Status: {r2.status_code}")
else:
    print("Variation 1 worked!")
