from gits_createrepo import create_github_repo
from gits_delete import delete_github_repo
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
    
test_create_repo()
def test_delete_repo() -> bool:
    repo_name = 'test'
    response = delete_github_repo(github_token, github_user, repo_name)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Error deleting repository. Status code: {response.status_code}")
        print(response.json())
    return True
  