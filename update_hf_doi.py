from huggingface_hub import HfApi, REMOVED_TOKEN_download
import os

# ==========================================
# PLEASE INSERT YOUR HUGGING FACE TOKEN HERE
# ==========================================
token = 'YOUR_HF_TOKEN' 

api = HfApi(token=token)

def update_repo_readme(repo_id, repo_type='model'):
    try:
        print(f"--- Processing {repo_id} ({repo_type}) ---")
        # Download existing README
        try:
            readme_path = REMOVED_TOKEN_download(repo_id=repo_id, repo_type=repo_type, filename="README.md", token=token)
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            content = "---\nlicense: mit\n---\n" # Default if not found
        
        doi_badge = "[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19743807-blue.svg)](https://doi.org/10.5281/zenodo.19743807)"
        citation_section = """
## 📜 Citation

If you use this framework or model in your research, please cite the official technical whitepaper:

```bibtex
@techreport{aclas_neuro_edu_2026,
  title={Neuro-Edu: A Cognitive Science-Driven Framework for Large Language Model Alignment in Educational Sandbox Simulation},
  author={Atlanta College of Liberal Arts and Sciences},
  year={2026},
  institution={ACLAS College},
  doi={10.5281/zenodo.19743807},
  url={https://doi.org/10.5281/zenodo.19743807}
}
```
"""

        # 1. Add DOI Badge to the top (after YAML header)
        if "zenodo.19743807" not in content:
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = "---" + parts[1] + "---\n\n" + doi_badge + "\n\n" + parts[2]
                else:
                    content = doi_badge + "\n\n" + content
            else:
                content = doi_badge + "\n\n" + content
            print("Added DOI badge.")

        # 2. Update placeholders
        old_placeholder = "10.5281/zenodo.aclascollege.neuro-edu.v1.0"
        if old_placeholder in content:
            content = content.replace(old_placeholder, "10.5281/zenodo.19743807")
            print("Replaced DOI placeholders.")

        # 3. Add Citation section if missing
        if "bibtex" not in content.lower():
            content = content.rstrip() + "\n" + citation_section
            print("Added Citation section.")

        # Upload back
        temp_filename = f"TEMP_README_{repo_id.replace('/', '_')}.md"
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(content)
        
        api.upload_file(
            path_or_fileobj=temp_filename,
            path_in_repo="README.md",
            repo_id=repo_id,
            repo_type=repo_type,
            commit_message="docs: Update official academic DOI and Citation info"
        )
        print(f"Successfully updated {repo_id}")
        os.remove(temp_filename)
        
    except Exception as e:
        print(f"Error updating {repo_id}: {e}")

if __name__ == '__main__':
    # Update core model and dashboard space
    update_repo_readme('ACLASCollege/neuro-edu-core-v3', repo_type='model')
    update_repo_readme('ACLASCollege/aclas-neuro-dashboard', repo_type='space')
