import requests

def get_github_branches(owner, repo, github_token):
    try:
        headers = {
            'Authorization': f'token {github_token}',
        }

        api_url = f'https://api.github.com/repos/{owner}/{repo}/branches'

        response = requests.get(api_url, headers=headers)
        return response

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


if __name__ == "__main__":
    owner = '  '
    repo = '  '
    github_token = '  ' 
    get_github_branches(owner, repo, token)
