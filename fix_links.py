import os
import glob

replacements = {
    "https://aclas.college/courses": "https://aclas.college/home/courses",
    "aclas.college/courses": "aclas.college/home/courses",
    "https://aclas.college/certification": "https://aclas.college/verify/certificate-verify",
    "aclas.college/certification": "aclas.college/verify/certificate-verify",
    "https://aclas.college/community": "https://aclas.college/admissions/alumni-network",
    "aclas.college/community": "aclas.college/admissions/alumni-network",
    "https://aclas.college/programs": "https://aclas.college/home/courses",
    "aclas.college/programs": "aclas.college/home/courses",
    "https://aclas.college/news": "https://aclas.college/blogs",
    "aclas.college/news": "aclas.college/blogs",
    "https://aclas.college/careers": "https://aclas.college/admissions/careers",
    "aclas.college/careers": "aclas.college/admissions/careers",
    "https://aclas.college/contact": "https://aclas.college/home/contact-us",
    "aclas.college/contact": "aclas.college/home/contact-us",
}

for filepath in glob.glob("**/*.md", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        with open(filepath, "w", encoding="utf-8", newline='\n') as f:
            f.write(content)
        print(f"Updated {filepath}")
