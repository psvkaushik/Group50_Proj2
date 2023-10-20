"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import requests


def get_github_diff(owner, repo, branch, github_token):
    """
    This function gets difference between the latest commit and the current state.
    owner: GitHub username
    repo: name of the GitHub repository 
    branch: branch you want to compare with the last commit
    github_token: user's PAT
    """
    try:
        headers = {
            'Authorization': f'token {github_token}',
        }

        url = f'https://api.github.com/repos/{owner}/{repo}/commits/{branch}'

        # Send a GET request to the GitHub API to retrieve the commit information.
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commit = response.json()
            commit_sha = commit['sha']

            diff_url = f'https://api.github.com/repos/{owner}/{repo}/compare/{commit_sha}...{branch}'

            response = requests.get(diff_url, headers=headers)
            if response.status_code == 200:
                diff_data = response.json()
                return diff_data['files']
            else:
                return f"Error: Unable to fetch the difference - Status Code {response.status_code}"

        else:
            return f"Error: Unable to fetch the latest commit - Status Code {response.status_code}"

    except Exception as e:
        print("ERROR: gits diff command caught an exception")
        return "ERROR: {}".format(str(e))

