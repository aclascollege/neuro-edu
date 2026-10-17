from huggingface_hub import HfApi

token = 'REMOVED_TOKEN'
api = HfApi(token=token)

def update_org_profile():
    org_name = 'ACLASCollege'
    description = "Atlanta College of Liberal Arts and Sciences (ACLAS) is a research-driven institution dedicated to democratizing elite education through autonomous cognitive AI simulation and on-device neural frameworks."
    
    try:
        # Note: 'interests' is not a standard field in update_organization API call 
        # but description/about is.
        api.update_organization(
            organization=org_name,
            description=description,
            fullname="ACLAS College"
        )
        print(f"Successfully updated {org_name} description and fullname.")
    except Exception as e:
        print(f"Error updating organization: {e}")

if __name__ == '__main__':
    update_org_profile()
