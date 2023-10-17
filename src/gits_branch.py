import requests

def get_github_branches(owner, repo, github_token):
    try:
        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub personal access token or use other authentication methods.
        headers = {
            'Authorization': f'token {github_token}',
        }

        # Define the API URL to list branches.
        api_url = f'https://api.github.com/repos/{owner}/{repo}/branches'

        # Send a GET request to the GitHub API.
        response = requests.get(api_url, headers=headers)
        return response
        #if response.status_code == 200:
        #    branches = response.json()
        #    branch_name = []
        #    for branch in branches:
        #        #print(branch['name'])
        #        branch_name.append(branch)
        #    return branch_name
        #else:
        #    print(f"Error: Unable to fetch branches - Status Code {response.status_code}")
        #    print(response.text)
        #   return False

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


if __name__ == "__main__":
    owner = '  '  # Replace with the GitHub username or organization name.
    repo = '  '  # Replace with the name of the GitHub repository.
    github_token = '  ' #Enter token here
    get_github_branches(owner, repo, token)
