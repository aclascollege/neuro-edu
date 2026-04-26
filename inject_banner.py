with open(r'd:\aicoding\kaiyuan\aclas-neuro-edu\README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
inserted = False
for line in lines:
    new_lines.append(line)
    if 'Atlanta College of Liberal Arts and Sciences (ACLAS)' in line and not inserted:
        new_lines.append('\n')
        new_lines.append('![ACLAS Neuro-Edu Social Preview](assets/social-preview.png)\n')
        inserted = True

with open(r'd:\aicoding\kaiyuan\aclas-neuro-edu\README.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("README updated with banner successfully!")
