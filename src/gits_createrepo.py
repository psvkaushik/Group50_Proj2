"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import requests


def create_github_repo(github_token, repo_name, git_license ='mit'):
    """

    Function to create a new github repo
    github_token : user's PAT token
    repo_name : name of the repo to be created
    git_license : the license to be used by the repo

    """
    headers = {
        'Authorization': f'token {github_token}',
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



