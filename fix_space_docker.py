from huggingface_hub import HfApi
import os

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

BANNER_URL = "https://huggingface.co/ACLASCollege/neuro-edu-core-v3/resolve/main/assets/banner.png"
DOI_BADGE = "[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19743807-blue.svg)](https://doi.org/10.5281/zenodo.19743807)"

def fix_space_docker():
    repo_id = 'ACLASCollege/aclas-neuro-dashboard'
    print(f"Fixing Space configuration as DOCKER for {repo_id}...")
    
    # Correct YAML for a Docker Space
    content = f"""---
title: Aclas Neuro Dashboard
emoji: 🐨
colorFrom: yellow
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

![ACLAS Banner]({BANNER_URL})

# ACLAS Neuro Dashboard

{DOI_BADGE}

Live 3D WebGL visualization and cognitive telemetry hub for the Neuro-Edu framework.

## 🔗 Resources
- **GitHub**: [aclascollege/neuro-edu](https://github.com/aclascollege/neuro-edu)
- **Organization**: [ACLAS College](https://huggingface.co/ACLASCollege)

## 📜 Citation
If you use this framework, please cite the official technical whitepaper:
```bibtex
@techreport{{aclas_neuro_edu_2026,
  title={{Neuro-Edu: A Cognitive Science-Driven Framework for Large Language Model Alignment in Educational Sandbox Simulation}},
  author={{Atlanta College of Liberal Arts and Sciences}},
  year={{2026}},
  institution={{ACLAS College}},
  doi={{10.5281/zenodo.19743807}},
  url={{https://doi.org/10.5281/zenodo.19743807}}
}}
```
"""
    
    with open("FIX_DOCKER_README.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    api.upload_file(
        path_or_fileobj="FIX_DOCKER_README.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type='space',
        commit_message="fix: Correct Space SDK to Docker and set app_port to 7860"
    )
    os.remove("FIX_DOCKER_README.md")
    print(f"Fixed {repo_id} with Docker config.")

if __name__ == '__main__':
    fix_space_docker()
