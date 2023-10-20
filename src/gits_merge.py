"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import requests


def merge_github_branch(repository_owner, repository_name, branch_name, access_token):
    #API endpoint for merging a branch
    url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/merges'
    
    commit_sha_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/git/refs/heads/{branch_name}'
    commit_sha_headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3.raw'
    }
    
    response = requests.get(commit_sha_url, headers=commit_sha_headers)

    if response.status_code == 200:
        latest_commit_sha = response.json()['object']['sha']
        # Data for the merge request
        data = {
            'base': 'main',
            'head': latest_commit_sha,
            'commit_message': 'Merge branch'
        }
        
        headers = {
            'Authorization': f'token {access_token}',
            'Accept': 'application/vnd.github.v3.raw'
        }
        #Headers with the PAT for authentication
        
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            return f"Branch '{branch_name}' merged successfully."
        else:
            return f"Failed to merge branch '{branch_name}'. Status code: {response.status_code}\n{response.text}"
    else:
        return f"Failed to get the latest commit SHA. Status code: {response.status_code}\n{response.text}"
