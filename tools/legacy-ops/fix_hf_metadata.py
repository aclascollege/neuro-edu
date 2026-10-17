from huggingface_hub import HfApi
import os

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def fix_profile_metadata():
    repo_id = 'ACLASCollege/README'
    
    print(f"Fixing metadata for {repo_id}...")
    
    # Download current content
    from huggingface_hub import REMOVED_TOKEN_download
    try:
        readme_path = REMOVED_TOKEN_download(repo_id=repo_id, repo_type='dataset', filename="README.md", token=token)
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return

    # Add YAML header if not present
    if not content.startswith("---"):
        yaml_header = """---
license: mit
task_categories:
- robotics
- other
language:
- en
- zh
tags:
- cognitive-science
- neuro-education
- multi-agent
- open-source
- aclas
---

"""
        content = yaml_header + content

    with open("FIX_PROFILE_README.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    api.upload_file(
        path_or_fileobj="FIX_PROFILE_README.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type='dataset',
        commit_message="fix: Add mandatory YAML metadata to profile README"
    )
    os.remove("FIX_PROFILE_README.md")
    print(f"Successfully fixed metadata for {repo_id}")

if __name__ == '__main__':
    fix_profile_metadata()
