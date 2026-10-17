import requests
import time
import os

token = os.getenv("GITHUB_TOKEN", "") # Securely loaded from environment
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user():
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code == 200:
        return response.json()["login"]
    else:
        print(f"Error getting user: {response.status_code} - {response.text}")
        return None

def submit_pr(target_owner, target_repo, entry_text, category_marker, section_name):
    my_user = get_user()
    if not my_user: return

    print(f"--- Processing {target_owner}/{target_repo} ---")
    
    # 1. Fork
    print(f"Forking {target_owner}/{target_repo}...")
    fork_resp = requests.post(f"https://api.github.com/repos/{target_owner}/{target_repo}/forks", headers=headers)
    if fork_resp.status_code not in [200, 202]:
        print(f"Fork failed: {fork_resp.status_code}")
        return

    # Wait for fork
    time.sleep(5)

    # 2. Get README
    print("Getting README content...")
    readme_resp = requests.get(f"https://api.github.com/repos/{my_user}/{target_repo}/contents/README.md", headers=headers)
    if readme_resp.status_code != 200:
        print(f"Failed to get README: {readme_resp.status_code}")
        return
    
    readme_data = readme_resp.json()
    import base64
    content = base64.b64decode(readme_data["content"]).decode('utf-8')
    sha = readme_data["sha"]

    # 3. Modify content
    if entry_text in content:
        print("Entry already exists in README.")
    else:
        # Find the category marker and insert after it
        if category_marker in content:
            print(f"Found {section_name} section. Inserting entry...")
            parts = content.split(category_marker, 1)
            # Insert after the marker + newline
            new_content = parts[0] + category_marker + "\n" + entry_text + "\n" + parts[1]
            
            # 4. Push update
            print("Pushing update to fork...")
            update_data = {
                "message": f"Add ACLAS Neuro-Edu SDK to {section_name}",
                "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
                "sha": sha
            }
            update_resp = requests.put(f"https://api.github.com/repos/{my_user}/{target_repo}/contents/README.md", headers=headers, json=update_data)
            if update_resp.status_code == 200:
                print("Update pushed successfully.")
                
                # 5. Create PR
                print("Creating Pull Request...")
                pr_data = {
                    "title": f"Add ACLAS Neuro-Edu SDK to {section_name}",
                    "head": f"{my_user}:master", # Assuming master, might be main
                    "base": "master",
                    "body": "Add ACLAS Neuro-Edu SDK to the list. It is an open-source framework for AI-powered education modeling human knowledge acquisition."
                }
                # Check if base is main
                repo_info = requests.get(f"https://api.github.com/repos/{target_owner}/{target_repo}", headers=headers).json()
                pr_data["base"] = repo_info["default_branch"]
                pr_data["head"] = f"{my_user}:{pr_data['base']}"

                pr_resp = requests.post(f"https://api.github.com/repos/{target_owner}/{target_repo}/pulls", headers=headers, json=pr_data)
                if pr_resp.status_code == 201:
                    print(f"Pull Request created: {pr_resp.json()['html_url']}")
                else:
                    print(f"PR creation failed: {pr_resp.status_code} - {pr_resp.text}")
            else:
                print(f"Update failed: {update_resp.status_code}")
        else:
            print(f"Could not find category marker: {category_marker}")

# Submission entries
ml_entry = "* [ACLAS Neuro-Edu SDK](https://github.com/aclascollege/neuro-edu) - Autonomous cognitive simulation framework for AI-powered education, modeling human knowledge acquisition with neural kernels and thermodynamic entropy analysis."
neuro_entry = "* [ACLAS Neuro-Edu SDK](https://github.com/aclascollege/neuro-edu) - Research-grade cognitive simulation framework by ACLAS College, integrating neural networks with educational psychology principles."

# Submit to ML
# Marker: #### General-Purpose Machine Learning
# (Note: In awesome-ml, there are multiple, we need the one under Python)
# Python marker is ## Python
submit_pr("josephmisiti", "awesome-machine-learning", ml_entry, "#### General-Purpose Machine Learning", "Python Machine Learning")

# Submit to Neuro
# Marker: ## Brain Simulation and Modeling
submit_pr("brandonhimpfen", "awesome-neuroscience", neuro_entry, "## Brain Simulation and Modeling", "Neuroscience Simulation")
