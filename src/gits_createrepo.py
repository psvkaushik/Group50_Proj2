import requests


def create_github_repo(PAT, repo_name, git_license ='mit'):
    """

    Function to create a new github repo
    PAT : user's PAT token
    repo_name : name of the repo to be created
    git_license : the license to be used by the repo

    """
    headers = {
        'Authorization': f'token {PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'name': repo_name,
        'license_template': git_license,
        'auto_init': True  # This will initialize the repository with a README.
    }


    url = f'https://api.github.com/user/repos'

    response = requests.post(url, headers=headers, json=data)
    return response



