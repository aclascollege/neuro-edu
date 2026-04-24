import urllib.request
import json
import base64
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

token = 'YOUR_HF_TOKEN'
repo_id = 'ACLASCollege/aclas-neuro-dashboard'
url = f'https://huggingface.co/api/spaces/{repo_id}/commit/main'

# Exact string with Unix newlines
raw_content = """---
title: Aclas Neuro Dashboard
emoji: 🐨
colorFrom: yellow
colorTo: blue
sdk: static
pinned: false
---

# ACLAS Neuro Dashboard
Live visualization for Neuro-Edu SDK.
"""

# Replace any Windows newlines just in case
raw_content = raw_content.replace('\r\n', '\n')

b64_content = base64.b64encode(raw_content.encode('utf-8')).decode('ascii')

payload = {
    "operations": [
        {
            "operation": "add",
            "path": "README.md",
            "content": b64_content,
            "encoding": "base64"
        }
    ],
    "commit_message": "fix: Restore static SDK configuration via API"
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), method='POST')
req.add_header('Authorization', f'Bearer {token}')
req.add_header('Content-Type', 'application/json')

try:
    res = urllib.request.urlopen(req, context=ctx)
    print("Success:", res.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8'))
