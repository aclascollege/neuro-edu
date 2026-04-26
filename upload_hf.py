from huggingface_hub import HfApi

token = 'YOUR_HF_TOKEN'
api = HfApi(token=token)

api.upload_file(
    path_or_fileobj='proper_REMOVED_TOKEN.md',
    path_in_repo='README.md',
    repo_id='ACLASCollege/aclas-neuro-dashboard',
    repo_type='space'
)
print("Uploaded successfully.")
