import requests
import yaml

def fork_repo(target_user, target_repo, user_token):
    """"
    Forks a repo from the target repo to the user's repo

    """
    headers = {
        "Accept": 'application/vnd.github.v3+json',
        "Authorization" : f'token {user_token}'
    }

    url = f'https://api.github.com/repos/{target_user}/{target_repo}/forks'

    response = requests.post(url, headers=headers)
    # success code is 202
    return response

# file_path = r'C:\Users\psvka\OneDrive\Desktop\fall23\se23\Group50_Proj2\vars.yaml'
# with open(file_path, 'r') as file:
#     data = yaml.safe_load(file)
# token = data['github_token']

# response = fork_repo('psvkaushik','ICR',token)
# print(response)