from huggingface_hub import HfApi

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def audit_repo(repo_id, repo_type='model'):
    try:
        files = api.list_repo_files(repo_id, repo_type=repo_type)
        print(f"Files in {repo_id}: {files}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    audit_repo('ACLASCollege/aclas-neuro-edu-demo')
