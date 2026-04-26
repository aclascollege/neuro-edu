from huggingface_hub import HfApi
import os

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def add_all_languages():
    repo_id = 'ACLASCollege/README'
    
    print(f"Adding all languages to {repo_id}...")
    
    # Download current content
    from huggingface_hub import REMOVED_TOKEN_download
    try:
        readme_path = REMOVED_TOKEN_download(repo_id=repo_id, repo_type='dataset', filename="README.md", token=token)
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return

    # Replace the language section in YAML
    new_lines = []
    in_yaml = False
    in_language = False
    
    languages_yaml = [
        "language:\n",
        "- en\n",
        "- zh\n",
        "- fr\n",
        "- es\n",
        "- ko\n",
        "- ja\n",
        "- ru\n",
        "- de\n"
    ]
    
    found_lang = False
    for line in lines:
        if line.strip() == "---":
            in_yaml = not in_yaml
            new_lines.append(line)
            continue
        
        if in_yaml and line.strip().startswith("language:"):
            in_language = True
            new_lines.extend(languages_yaml)
            found_lang = True
            continue
            
        if in_language:
            if line.strip().startswith("- ") and len(line.strip()) <= 5: # Simple heuristic for lang codes
                continue
            else:
                in_language = False
                new_lines.append(line)
        else:
            new_lines.append(line)

    if not found_lang:
        # If no language section found, insert it before the closing ---
        last_dash = -1
        for i, line in enumerate(new_lines):
            if line.strip() == "---":
                last_dash = i
        if last_dash != -1:
            for l in reversed(languages_yaml):
                new_lines.insert(last_dash, l)

    with open("FIX_LANGS_README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
        
    api.upload_file(
        path_or_fileobj="FIX_LANGS_README.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type='dataset',
        commit_message="docs: Add all 8 supported languages to metadata"
    )
    os.remove("FIX_LANGS_README.md")
    print(f"Successfully added all languages to {repo_id}")

if __name__ == '__main__':
    add_all_languages()
