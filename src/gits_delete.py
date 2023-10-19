"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com
"""

import requests

def delete_github_repo(github_token, user_name, repo_name_to_delete):
    """

    Function to delete a  github repo
    github_token : user's PAT token
    user_name : the github username
    repo_name_to_delete : name of the repo to be created
    

    """
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{user_name}/{repo_name_to_delete}'

    response = requests.delete(url, headers=headers)
    
    
    return response
