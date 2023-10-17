from gits_createrepo import create_github_repo
from gits_delete import delete_github_repo
from gits_fork import fork_repo
from gits_checkbranch import check_branch_exists

import os

github_token = os.environ['GITS_GITHUB_TOKEN']
github_user = 'GITSSE23'


def test_create_repo() -> bool:
    repo_name = 'test'

    response = create_github_repo(github_token, repo_name)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        
    elif response.status_code == 422:
        print(f'Repo called {repo_name} already exists -----')
    else:
        print(f"Error creating repository. Status code: {response.status_code}")
        print(response.json())
    return True
    

def test_delete_repo() -> bool:
    repo_name = 'test'
    response = delete_github_repo(github_token, github_user, repo_name)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Error deleting repository. Status code: {response.status_code}")
        print(response.json())
    return True
  
def test_fork() -> bool:
    repo_name = 'slash'
    user_name = 'TommasU'
    response = fork_repo(user_name, repo_name, github_token)
    if response.status_code == 202:
        print(f"Repository '{user_name}/{repo_name}' forked successfully!")
    else:
        print(f"Error deleting repository. Status code: {response.status_code}")
        print(response.json())
    return True

def test_check_branch() -> bool:
    branch_name = 'main'
    username = 'GITSSE23'
    reponame = 'test2'
    branch_name = 'newb'
    response = check_branch_exists(github_token, username, reponame, branch_name)
    if response.status_code == 200:
        print('The branch {branchname} exists.')
    else:
        print(f"Error deleting repository. Status code: {response.status_code}")
        print(response.json())
    return True

