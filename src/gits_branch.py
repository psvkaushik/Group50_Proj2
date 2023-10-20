"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import requests

def get_github_branches(owner, repo_name, github_token):
    """
    Function to list out all the branches in a repository

    owner: the username of the repo's owner
    repo_name: name of the repo
    github_token: user's PAT
    """
    try:
        headers = {
            'Authorization': f'token {github_token}',
        }

        api_url = f'https://api.github.com/repos/{owner}/{repo_name}/branches'

        response = requests.get(api_url, headers=headers)
        return response

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False


