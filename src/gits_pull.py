import requests
import os
import zipfile

def download_github_repo(token, repo_owner, repo_name, local_dir):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3.raw'
    }

    # Create a ZIP archive URL for the GitHub repository
    repo_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/zipball/main'

    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        zip_filename = os.path.join(local_dir, f'{repo_name}_main.zip')

        with open(zip_filename, 'wb') as zip_file:
            zip_file.write(response.content)

        # Extract the ZIP archive to the local directory
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(local_dir)

        # Clean up the ZIP file
        os.remove(zip_filename)

        print(f"Repository '{repo_name}' successfully downloaded and extracted to '{local_dir}'")
    else:
        print(f"Error downloading the repository. Status code: {response.status_code}")
        print(response.text)

# Replace with your GitHub Personal Access Token
github_token = ' '   ###enter github token

# Replace with the repository owner and name
repo_owner = ' '   ### username of the owner
repo_name = '  '   ### Repository name

# Replace with the local directory where you want to save the repository
local_dir = '   '   ###local directory to save the repo

download_github_repo(github_token, repo_owner, repo_name, local_dir)
