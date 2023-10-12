from create_repo import create_github_repo
import os

github_token = os.environ['GITS_GITHUB_TOKEN']


def test_create_repo() -> bool:
    repo_name = 'test'
    response = create_github_repo(github_token, repo_name)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return True
    else:
        print(f"Error creating repository. Status code: {response.status_code}")
        print(response.json())
        return False
def test_delete_repo() -> bool:
    return False
  