import requests
#from read_token import github_token
import yaml

def create_github_repo(token, repo_name):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'name': repo_name,
        'auto_init': True  # This will initialize the repository with a README. You can customize this as needed.
    }

    # Replace 'your_username' with your GitHub username
    url = f'https://api.github.com/user/repos'

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Error creating repository. Status code: {response.status_code}")
        print(response.json())
    return response

# Replace 'your_repo_name' with the desired repository name
# repo_name = 'test'

# file_path = r'C:\Users\psvka\OneDrive\Desktop\fall23\se23\Group50_Proj2\vars.yaml'
# with open(file_path, 'r') as file:
#     data = yaml.safe_load(file)
# token = data['github_token']
# create_github_repo(token, repo_name)

