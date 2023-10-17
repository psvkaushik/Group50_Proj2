import requests


def get_github_commit_diff(owner, repo, branch, github_token):
    try:
        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub personal access token or use other authentication methods.
        headers = {
            'Authorization': f'token {github_token}',  ####TOKEN
        }

        # Define the API URL to fetch the latest commit on a specific branch.
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{branch}'

        # Send a GET request to the GitHub API to retrieve the commit information.
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            commit = response.json()
            commit_sha = commit['sha']

            # Define the API URL to get the difference between the latest commit and the current state.
            diff_api_url = f'https://api.github.com/repos/{owner}/{repo}/compare/{commit_sha}...{branch}'

            # Send a GET request to the GitHub API to retrieve the difference.
            response = requests.get(diff_api_url, headers=headers)
            return response
            #if response.status_code == 200:
            #    diff_data = response.json()
            #    print("Difference since the last commit:")
            #    print(diff_data['files'])
            #else:
            #    print(f"Error: Unable to fetch the difference - Status Code {response.status_code}")
            #    print(response.text)
            #    return False
        else:
            #print(f"Error: Unable to fetch the latest commit - Status Code {response.status_code}")
            #print(response.text)
            #return False
            return response

    except Exception as e:
        print("ERROR: gits diff command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


if __name__ == "__main__":
    owner = ' '  # Replace with your GitHub username or organization name.
    repo = ' '  # Replace with the name of the GitHub repository.
    branch = ' '  # Specify the branch you want to compare with the last commit.
    github_token = '  '  # Enter token 

    get_github_commit_diff(owner, repo, branch)
