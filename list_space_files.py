from huggingface_hub import HfApi

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def list_space_files():
    repo_id = 'ACLASCollege/aclas-neuro-dashboard'
    try:
        files = api.list_repo_files(repo_id, repo_type='space')
        print(f"Files in Space {repo_id}: {files}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_space_files()
