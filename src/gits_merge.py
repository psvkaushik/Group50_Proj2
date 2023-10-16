import requests

#Inputs to the code:
repository_owner = 'VaishnaviNaik96'
repository_name = 'test_510'
branch_name = 'test'

#Personal Access Token - Generate one in your GitHub account with the "repo" scope
access_token = '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'

# API endpoint for merging a branch
url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/merges'

commit_sha_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/git/refs/heads/{branch_name}' #SHA of latest commit on the 'test' branch
commit_sha_headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3.raw'
}

response = requests.get(commit_sha_url, headers=commit_sha_headers)

if response.status_code == 200:
    latest_commit_sha = response.json()['object']['sha']
    #data for the merge request
    data = {
        'base': 'main',  #target branch to merge into
        'head': latest_commit_sha,  #SHA of 'test' branch
        'commit_message': 'Merge branch'  #commit message for the merge
    }
    
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3.raw'
    }
    #headers with the PAT for authentication
    
    response = requests.post(url, headers=headers, json=data) #POST request to merge the branch

    if response.status_code == 201:
        print(f"Branch '{branch_name}' merged successfully.")
    else:
        print(f"Failed to merge branch '{branch_name}'. Status code: {response.status_code}")
        print(response.text)
else:
    print(f"Failed to get the latest commit SHA. Status code: {response.status_code}")
    print(response.text)
