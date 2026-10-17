from huggingface_hub import HfApi
import json

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def audit_REMOVED_TOKEN(org_name):
    audit_results = {
        "models": [],
        "spaces": [],
        "datasets": []
    }
    
    # Audit Models
    models = api.list_models(author=org_name)
    for m in models:
        files = api.list_repo_files(m.id)
        audit_results["models"].append({
            "id": m.id,
            "tags": m.tags,
            "has_readme": "README.md" in files,
            "last_modified": m.last_modified
        })
        
    # Audit Spaces
    spaces = api.list_spaces(author=org_name)
    for s in spaces:
        files = api.list_repo_files(s.id, repo_type='space')
        audit_results["spaces"].append({
            "id": s.id,
            "sdk": s.sdk,
            "has_readme": "README.md" in files,
            "last_modified": s.last_modified
        })
        
    return audit_results

if __name__ == '__main__':
    results = audit_REMOVED_TOKEN('ACLASCollege')
    with open('REMOVED_TOKEN_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, default=str)
    print("HF Audit complete. Results saved to REMOVED_TOKEN_results.json")
