import os

def add_doi_to_translations():
    doi_badge = '\n[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19743807-blue.svg)](https://doi.org/10.5281/zenodo.19743807)\n'
    
    translations_dir = 'translations'
    if not os.path.exists(translations_dir):
        print("Translations directory not found.")
        return
        
    files = [f for f in os.listdir(translations_dir) if f.endswith('.md')]
    
    for filename in files:
        filepath = os.path.join(translations_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Check if DOI already exists
        content = "".join(lines)
        if 'zenodo.19743807' in content:
            print(f"DOI already in {filename}, skipping.")
            continue
            
        # Find the first '---' line (usually line 11)
        # Or just insert after the header info
        inserted = False
        for i, line in enumerate(lines):
            if '---' in line:
                lines.insert(i + 1, doi_badge)
                inserted = True
                break
        
        if inserted:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f"Added DOI to {filename}")
        else:
            print(f"Could not find insertion point in {filename}")

if __name__ == '__main__':
    add_doi_to_translations()
