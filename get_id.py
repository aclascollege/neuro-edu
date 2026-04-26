import requests

api_key = "MCJzWCZDpiJTgi8EmYiwh1D1"
url = "https://dev.to/api/articles/aclas_college/deep-dive-the-cognitive-science-behind-the-aclas-neuro-edu-sdk-179c"

response = requests.get(url)
if response.status_code == 200:
    print("ID:", response.json().get("id"))
else:
    print("Error:", response.status_code)
