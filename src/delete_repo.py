import requests
import yaml

def delete_github_repo(auth_token, user,  repo_name_to_delete):
    headers = {
        'Authorization': f'token {auth_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{user}/{repo_name_to_delete}'

    response = requests.delete(url, headers=headers)
    

    return response

    


# file_path = r'C:\Users\psvka\OneDrive\Desktop\fall23\se23\Group50_Proj2\vars.yaml'
# with open(file_path, 'r') as file:
#     data = yaml.safe_load(file)
# token = data['github_token']
# #Replace 'your_repo_name' with the name of the repository you want to delete
# repo_name = 'test3'
# username = 'GITSSE23'
# delete_github_repo(token, username, repo_name)
