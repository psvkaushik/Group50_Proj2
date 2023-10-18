import requests


def count_commits_in_github_repo(repo_url):
    global response
    parts = repo_url.rstrip('/').split('/')
    owner = parts[-2]
    repo_name = parts[-1]

    commit_count = 0
    page = 1
    per_page = 100

    try:
        while True:
            api_url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
            params = {'page': page, 'per_page': per_page}
            response = requests.get(api_url, params=params) 
            response.raise_for_status() 
            commits = response.json() 
            commit_count += len(commits) 
            if len(commits) < per_page:
                break
            page += 1
        return str(commit_count)

    except requests.exceptions.RequestException as e:
         return f"Error fetching commit count"

if __name__ == '__main__':
    repo_url = input("Enter the public GitHub repository URL: ")
    commit_count = str(count_commits_in_github_repo(repo_url))
