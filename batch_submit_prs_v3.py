import requests
import json
import time
import base64
import os

token = os.getenv("GITHUB_TOKEN", "") # Securely loaded from environment
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user():
    response = requests.get("https://api.github.com/user", headers=headers)
    return response.json()["login"] if response.status_code == 200 else None

my_user = get_user()

def submit_to_list(owner, repo, marker, entry, section_name):
    print(f"\n>>> Processing {owner}/{repo} ({section_name})")
    
    # 1. Fork
    print(f"Forking...")
    fork_resp = requests.post(f"https://api.github.com/repos/{owner}/{repo}/forks", headers=headers)
    if fork_resp.status_code not in [200, 202]:
        print(f"Fork failed: {fork_resp.status_code}")
        return
    
    time.sleep(10) # Wait for fork to propagate

    # 2. Get README
    readme_resp = requests.get(f"https://api.github.com/repos/{my_user}/{repo}/contents/README.md", headers=headers)
    if readme_resp.status_code != 200:
        print(f"Failed to get README from fork.")
        return

    readme_data = readme_resp.json()
    content = base64.b64decode(readme_data["content"]).decode('utf-8')
    sha = readme_data["sha"]

    if entry in content:
        print("Entry already exists.")
        return

    # 3. Modify
    if marker in content:
        print(f"Found marker '{marker}'. Injecting...")
        parts = content.split(marker, 1)
        new_content = parts[0] + marker + "\n" + entry + "\n" + parts[1]
        
        # 4. Push
        update_data = {
            "message": f"Add ACLAS Neuro-Edu SDK to {section_name}",
            "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
            "sha": sha
        }
        update_resp = requests.put(f"https://api.github.com/repos/{my_user}/{repo}/contents/README.md", headers=headers, json=update_data)
        if update_resp.status_code == 200:
            print(f"✅ Successfully updated your fork: {my_user}/{repo}")
            print(f"🔗 Ready for PR: https://github.com/aclascollege/{repo}/compare/master...aclascollege:master")
        else:
            print(f"Update failed: {update_resp.status_code}")
    else:
        print(f"Marker '{marker}' not found. Attempting fuzzy match...")
        # Fallback to similar header if possible
        if marker.replace("#", "").strip() in content:
             print("Fuzzy match found. Proceeding with caution.")
             # ... more logic could go here
        else:
             print(f"Could not find exact section: {marker}")

# Entry
standard_entry = "* [ACLAS Neuro-Edu SDK](https://github.com/aclascollege/neuro-edu) - Autonomous cognitive simulation framework for AI-powered education, modeling human knowledge acquisition with neural kernels and thermodynamic entropy analysis."

targets = [
    ("KennethanCeyer", "awesome-numpy", "### AI/ML", "NumPy AI"),
    ("hkalant", "awesome-edtech-tools", "### Coding/Programming Schools", "EdTech Tools"),
    ("abi-aryan", "awesome-cogsci", "# Relevant Resources", "CogSci Resources"),
    ("sakimarquis", "awesome-computational-neuroscience", "### Simulation", "CompNeuro Simulation"),
    ("owainlewis", "awesome-artificial-intelligence", "## Libraries", "General AI")
]

for owner, repo, marker, section in targets:
    try:
        submit_to_list(owner, repo, marker, standard_entry, section)
    except Exception as e:
        print(f"Error processing {repo}: {e}")
    time.sleep(5)
