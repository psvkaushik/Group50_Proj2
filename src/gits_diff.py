"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import requests


def get_github_diff(owner, repo, branch, github_token):
    try:
        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub personal access token or use other authentication methods.
        headers = {
            'Authorization': f'token {github_token}',
        }

        # Define the API URL to fetch the latest commit on a specific branch.
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{branch}'

        # Send a GET request to the GitHub API to retrieve the commit information.
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            commit = response.json()
            commit_sha = commit['sha']

            diff_api_url = f'https://api.github.com/repos/{owner}/{repo}/compare/{commit_sha}...{branch}'

            response = requests.get(diff_api_url, headers=headers)
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


if __name__ == "__main__":
    owner = ' '
    repo = ' '
    branch = ' '
    github_token = '  '

    get_github_diff(owner, repo, branch)
