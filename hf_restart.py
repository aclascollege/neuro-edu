from huggingface_hub import HfApi

token = 'YOUR_HF_TOKEN'
api = HfApi(token=token)

repo_id = 'ACLASCollege/aclas-neuro-dashboard'

try:
    print("Attempting to factory reboot the Space...")
    api.restart_space(repo_id=repo_id, factory_reboot=True)
    print("Factory reboot triggered successfully.")
except Exception as e:
    print("Error during factory reboot:", e)
    
    try:
        print("Attempting standard restart...")
        api.restart_space(repo_id=repo_id)
        print("Standard restart triggered successfully.")
    except Exception as e2:
        print("Error during standard restart:", e2)
