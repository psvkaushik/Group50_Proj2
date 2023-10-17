import requests

def check_branch_exists(PAT, user_name, repo_name, branch_name):
    """
    Function to check if a branch exists or not
    PAT : user's PAT
    branch_name : the name of the branch whose existence is in question
    user_name : url of the repository on which the branch existence is checked 
    """
    headers = {
        "Accept": 'application/vnd.github.v3+json',
        "Authorization" : f'token {PAT}'
    }

    url = f'https://api.github.com/repos/{user_name}/{repo_name}/branches/{branch_name}'

    response = requests.get(url=url, headers=headers)
    return response

print(check_branch_exists('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', 'GITSSE23', 'test2', 'main'))

