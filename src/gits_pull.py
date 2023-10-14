import requests

def pull_file_from_github(token, repo_owner, repo_name, filename, local_filepath):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3.raw'  # Request raw content
    }

    file_url = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{filename}'

    response = requests.get(file_url, headers=headers)

    if response.status_code == 200:
        with open(local_filepath, 'w') as local_file:
            local_file.write(response.text)
        print(f"File '{filename}' successfully pulled to '{local_filepath}'")
    else:
        print(f"Error pulling the file. Status code: {response.status_code}")
        print(response.text)

# Replace with your GitHub Personal Access Token
# github_token = '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'

# Replace with the repository owner and name
repo_owner = 'VaishnaviNaik96'
repo_name = 'test_510'

# Replace with the name of the text file you want to pull
filename = 'testing'

# Replace with the local path where you want to save the file
local_filepath = 'local_example.txt'

pull_file_from_github(github_token, repo_owner, repo_name, filename, local_filepath)
