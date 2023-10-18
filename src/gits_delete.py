"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import requests

def delete_github_repo(PAT, username, repo_name_to_delete):
    """

    Function to delete a  github repo
    PAT : user's PAT token
    username : the 
    repo_name_to_delete : name of the repo to be created
    

    """
    headers = {
        'Authorization': f'token {PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{username}/{repo_name_to_delete}'

    response = requests.delete(url, headers=headers)
    
    
    return response
