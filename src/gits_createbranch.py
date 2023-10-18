import requests
from gits_checkbranch import check_branch_exists

def create_branch(username, repo_name, base_branch, new_branch, PAT):
    """
    Creates the new_branch off of the base_branch
    username: The user's GitHub username
    repo_name: The name of the repo on which the branch is created
    base_branch: The branch on which the new branch is created
    new_branch: name of the new branch to be created
    PAT: The PAT of the user
    """

    url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {PAT}"
    }

    # Check if the base branch exists before trying to branch off of it
    response = check_branch_exists(PAT, username, repo_name, base_branch)
    if response.status_code == 200:
        base_branch_url = f"https://api.github.com/repos/{username}/{repo_name}/branches/{base_branch}"
        base_branch_response = requests.get(base_branch_url, headers=headers).json()
        sha = base_branch_response['commit']['sha']
        data = {
            "ref": f"refs/heads/{new_branch}",
            "sha": sha
        }

        response = requests.post(url, headers=headers, json=data)
    return response