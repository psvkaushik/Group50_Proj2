"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com
"""

import requests

def fork_repo(target_user, target_repo, PAT):
    """"
    Forks a repo from the target repo to the user's repo
    target_user : username of the user who's repo you want to fork
    target_repo : name of the Repo which is to be forked
    PAT : personal PAT

    """
    headers = {
        "Accept": 'application/vnd.github.v3+json',
        "Authorization" : f'token {PAT}'
    }

    url = f'https://api.github.com/repos/{target_user}/{target_repo}/forks'

    response = requests.post(url, headers=headers)
    
    return response
