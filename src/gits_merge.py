import requests

#Inputs to the code:
repository_owner = ' ' ##OWNER NAME
repository_name = '  ' ##REPO NAME
branch_name = ' ' ##BRANCH YOU WANT TO MERGE INTO MAIN

#Personal Access Token - Generate one in your GitHub account with the "repo" scope
access_token = ' ' ##TOKEN

def merge_github_branch(repository_owner, repository_name, branch_name, access_token):
    #API endpoint for merging a branch
    url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/merges'
    
    commit_sha_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/git/refs/heads/{branch_name}' # SHA of the latest commit on the 'test' branch
    commit_sha_headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3.raw'
    }
    
    response = requests.get(commit_sha_url, headers=commit_sha_headers)

    if response.status_code == 200:
        latest_commit_sha = response.json()['object']['sha']
        # Data for the merge request
        data = {
            'base': 'main',  #target is the main branch
            'head': latest_commit_sha,  #SHA of 'test' branch
            'commit_message': 'Merge branch'  #commit message for the merge
        }
        
        headers = {
            'Authorization': f'token {access_token}',
            'Accept': 'application/vnd.github.v3.raw'
        }
        #Headers with the PAT for authentication
        
        response = requests.post(url, headers=headers, json=data) #POST request to merge the branch

        if response.status_code == 201:
            return f"Branch '{branch_name}' merged successfully."
        else:
            return f"Failed to merge branch '{branch_name}'. Status code: {response.status_code}\n{response.text}"
    else:
        return f"Failed to get the latest commit SHA. Status code: {response.status_code}\n{response.text}"
