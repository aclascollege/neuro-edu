import json
import base64

readme_content = """---
title: Aclas Neuro Dashboard
emoji: 🧠
colorFrom: yellow
colorTo: blue
sdk: docker
pinned: false
---

# ACLAS Neuro Dashboard
Live visualization for Neuro-Edu SDK.
"""

dockerfile_content = """FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
"""

b64_readme = base64.b64encode(readme_content.encode('utf-8')).decode('ascii')
b64_dockerfile = base64.b64encode(dockerfile_content.encode('utf-8')).decode('ascii')

payload = {
  "operations": [
    {
      "operation": "add",
      "path": "README.md",
      "content": b64_readme,
      "encoding": "base64"
    },
    {
      "operation": "add",
      "path": "Dockerfile",
      "content": b64_dockerfile,
      "encoding": "base64"
    }
  ],
  "summary": "Force transition to Docker SDK with proper entrypoint"
}

with open('hf_final_docker_payload.json', 'w', encoding='utf-8') as f:
    json.dump(payload, f)

print("Generated hf_final_docker_payload.json")
