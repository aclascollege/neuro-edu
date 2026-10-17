from huggingface_hub import HfApi
import os

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def create_profile_readme():
    repo_id = 'ACLASCollege/README'
    org_name = 'ACLASCollege'
    
    print(f"Creating profile README repository: {repo_id}...")
    
    try:
        api.create_repo(repo_id=repo_id, repo_type='dataset', exist_ok=True)
    except Exception as e:
        print(f"Error creating repo: {e}")

    # Adapt content from local aclascollege/README.md
    github_readme_path = r'd:\aicoding\kaiyuan\aclascollege\README.md'
    if os.path.exists(github_readme_path):
        with open(github_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# ACLAS College\nDemocratizing world-class education through Autonomous AI Simulation."

    # Add HF specific banner and formatting
    banner_url = "https://huggingface.co/ACLASCollege/neuro-edu-core-v3/resolve/main/assets/banner.png"
    
    # Remove the existing logo/header part and replace with the high-tech banner
    if '<div align="center">' in content:
        parts = content.split('</div>', 1)
        if len(parts) > 1:
            header = f"""<div align="center">
<img src="{banner_url}" width="100%" alt="ACLAS Banner" />
<br>
<h1>Atlanta College of Liberal Arts and Sciences (ACLAS)</h1>
<h3><i>Democratizing world-class education through Autonomous AI Simulation.</i></h3>
"""
            content = header + parts[1]

    with open("HF_PROFILE_README.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    api.upload_file(
        path_or_fileobj="HF_PROFILE_README.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type='dataset',
        commit_message="docs: Initialize Hugging Face organization profile README"
    )
    os.remove("HF_PROFILE_README.md")
    print(f"Successfully initialized {repo_id}")

if __name__ == '__main__':
    create_profile_readme()
