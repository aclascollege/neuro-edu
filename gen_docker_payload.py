import json
import base64

content = """---
title: Aclas Neuro Dashboard
emoji: 🐨
colorFrom: yellow
colorTo: blue
sdk: docker
pinned: false
---

# ACLAS Neuro Dashboard
Live visualization for Neuro-Edu SDK.
"""

b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')

payload = {
  "operations": [
    {
      "operation": "add",
      "path": "README.md",
      "content": b64,
      "encoding": "base64"
    }
  ],
  "summary": "Force state change to docker"
}

with open('hf_docker_payload_correct.json', 'w', encoding='utf-8') as f:
    json.dump(payload, f)
