from huggingface_hub import HfApi
import os

token = 'YOUR_HF_TOKEN'
api = HfApi(token=token)

BANNER_URL = "https://huggingface.co/ACLASCollege/neuro-edu-core-v3/resolve/main/assets/banner.png"
DOI_LINK = "https://doi.org/10.5281/zenodo.19743807"
DOI_BADGE = f"[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19743807-blue.svg)]({DOI_LINK})"

COMMON_TAGS = [
    "cognitive-science", "education", "multi-agent", "neuroscience", 
    "open-source", "research", "neuro-edu", "aclas", "llama-3", 
    "qwen", "deepseek", "gemma", "phi-3", "mistral"
]

CITATION = f"""
## 📜 Citation
If you use this framework, please cite the official technical whitepaper:
```bibtex
@techreport{{aclas_neuro_edu_2026,
  title={{Neuro-Edu: A Cognitive Science-Driven Framework for Large Language Model Alignment in Educational Sandbox Simulation}},
  author={{Atlanta College of Liberal Arts and Sciences}},
  year={{2026}},
  institution={{ACLAS College}},
  doi={{10.5281/zenodo.19743807}},
  url={{{DOI_LINK}}}
}}
```
"""

def polish_repo(repo_id, title, description, repo_type='model', extra_content=""):
    print(f"Polishing {repo_id}...")
    
    # Metadata Header
    yaml_header = f"""---
license: mit
language:
- en
- zh
- fr
- es
- ko
- ja
- ru
- de
tags:
{chr(10).join(['- ' + t for t in COMMON_TAGS])}
metrics:
- accuracy
- knowledge_retention
---
"""

    content = f"""{yaml_header}

![ACLAS Banner]({BANNER_URL})

# {title}

{DOI_BADGE}

{description}

{extra_content}

## 🔗 Resources
- **GitHub**: [aclascollege/neuro-edu](https://github.com/aclascollege/neuro-edu)
- **Organization**: [ACLAS College](https://huggingface.co/ACLASCollege)

{CITATION}
"""
    
    with open("TEMP_POLISH.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    api.upload_file(
        path_or_fileobj="TEMP_POLISH.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type=repo_type,
        commit_message="docs: Final professional polish with banner, DOI and SEO tags"
    )
    os.remove("TEMP_POLISH.md")
    print(f"Finished {repo_id}")

if __name__ == '__main__':
    # 1. Upload Banner Asset
    banner_path = r'C:\Users\86187\.gemini\antigravity\brain\20b044ee-a001-4964-9f05-4c81daa5bc2e\REMOVED_TOKEN_banner_1777063447512.png'
    if os.path.exists(banner_path):
        api.upload_file(
            path_or_fileobj=banner_path,
            path_in_repo="assets/banner.png",
            repo_id="ACLASCollege/neuro-edu-core-v3",
            repo_type="model",
            commit_message="assets: Upload organization banner"
        )
        print("Banner uploaded.")

    # 2. Polish Core Model
    polish_repo(
        'ACLASCollege/neuro-edu-core-v3',
        'ACLAS Neuro-Edu Core v3.0',
        'Autonomous Cognitive Simulation Framework for AI-Powered Education. The core engine for on-device neural simulations.'
    )

    # 3. Polish Dashboard Space
    polish_repo(
        'ACLASCollege/aclas-neuro-dashboard',
        'ACLAS Neuro Dashboard',
        'Live 3D WebGL visualization and cognitive telemetry hub for the Neuro-Edu framework.',
        repo_type='space'
    )

    # 4. Polish/Initialize Demo Repo
    polish_repo(
        'ACLASCollege/aclas-neuro-edu-demo',
        'ACLAS Neuro-Edu Demo',
        'A lightweight demonstration model and sample data for the Neuro-Edu SDK, optimized for rapid prototyping.'
    )
