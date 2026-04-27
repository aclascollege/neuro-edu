import os

def add_doi_badge():
    doi_badge = '[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19743807.svg)](https://doi.org/10.5281/zenodo.19743807)\n'
    
    files = [os.path.join('translations', f) for f in os.listdir('translations') if f.endswith('.md')]
    
    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'zenodo.19743807' in content:
            continue
            
        # Find the start of badges (usually after the first hr ---)
        # or just before the License badge
        if '[![License' in content:
            new_content = content.replace('[![License', doi_badge + '[![License')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added DOI to {filepath}")
        else:
            print(f"Could not find license badge in {filepath}")

if __name__ == '__main__':
    add_doi_badge()
