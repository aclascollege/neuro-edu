from huggingface_hub import HfApi
import os

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

# Helper to get raw URL for HF assets
def get_asset_url(repo_id, filename):
    return f"https://huggingface.co/ACLASCollege/neuro-edu-core-v3/resolve/main/assets/{filename}"

def update_REMOVED_TOKEN():
    # 1. Upload all 3 specific banners to the main assets repo (neuro-edu-core-v3)
    asset_dir = 'assets'
    for img in ['og_sdk_preview.png', 'og_model_preview.png', 'og_dashboard_preview.png']:
        local_path = os.path.join(asset_dir, img)
        if os.path.exists(local_path):
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=f"assets/{img}",
                repo_id="ACLASCollege/neuro-edu-core-v3",
                repo_type="model",
                commit_message=f"assets: Add specific social preview {img}"
            )
            print(f"Uploaded {img}")

    # 2. Update each README with its specific banner
    repos = [
        {
            "id": "ACLASCollege/neuro-edu-core-v3",
            "type": "model",
            "banner": "og_model_preview.png",
            "title": "ACLAS Neuro-Edu Core v3.0"
        },
        {
            "id": "ACLASCollege/aclas-neuro-dashboard",
            "type": "space",
            "banner": "og_dashboard_preview.png",
            "title": "ACLAS Neuro Dashboard"
        },
        {
            "id": "ACLASCollege/aclas-neuro-edu-demo",
            "type": "model",
            "banner": "og_sdk_preview.png",
            "title": "ACLAS Neuro-Edu Demo"
        }
    ]

    for repo in repos:
        print(f"Updating banner for {repo['id']}...")
        try:
            from huggingface_hub import REMOVED_TOKEN_download
            readme_path = REMOVED_TOKEN_download(repo_id=repo['id'], repo_type=repo['type'], filename="README.md", token=token)
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace the generic banner with specific one
            old_banner_marker = "![ACLAS Banner]"
            new_banner = f"![{repo['title']}]({get_asset_url('ACLASCollege/neuro-edu-core-v3', repo['banner'])})"
            
            if old_banner_marker in content:
                # Find the line with the old banner and replace it
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if old_banner_marker in line:
                        lines[i] = new_banner
                        break
                content = '\n'.join(lines)
            else:
                # If no banner, insert after YAML
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        content = "---" + parts[1] + "---\n\n" + new_banner + "\n\n" + parts[2]
                else:
                    content = new_banner + "\n\n" + content
            
            with open("TEMP_VISUAL.md", "w", encoding="utf-8") as f:
                f.write(content)
            
            api.upload_file(
                path_or_fileobj="TEMP_VISUAL.md",
                path_in_repo="README.md",
                repo_id=repo['id'],
                repo_type=repo['type'],
                commit_message="docs: Update specific social preview banner"
            )
            print(f"Successfully updated {repo['id']}")
            os.remove("TEMP_VISUAL.md")
        except Exception as e:
            print(f"Error updating {repo['id']}: {e}")

if __name__ == '__main__':
    update_REMOVED_TOKEN()
