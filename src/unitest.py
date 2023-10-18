import unittest
from unittest.mock import Mock, patch
import subprocess

from gits_createrepo import create_github_repo
from gits_branch import get_github_branches
from gits_checkbranch import check_branch_exists
from gits_delete import delete_github_repo
from gits_diff import get_github_commit_diff
from gits_fork import fork_repo
from gits_merge import merge_github_branch
from gits_pull import download_github_repo
#from read_token import  username
from gits_clone import clone_repository

import os
# github_token = os.environ["GITS_GITHUB_TOKEN"]

github_token = "jfjyYVpBmGnGdueNlhEH6skTDKaUbH2hP5xC"
username = 'GITSSE23'

class TestCreateGithubRepo(unittest.TestCase):

    @patch('requests.post')
    def test_successful_repo_creation(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        token = github_token
        repo_name = 'test_repo'

        # Act
        response = create_github_repo(token, repo_name)

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertTrue(mock_post.called)
        return True

    @patch('requests.post')
    def test_failed_repo_creation(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 400  # Simulating an error status code
        mock_response.json.return_value = {'message': 'Repository already exists'}
        mock_post.return_value = mock_response

        token = github_token
        repo_name = 'existing_repo'

        # Act
        response = create_github_repo(token, repo_name)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertTrue(mock_post.called)
        return False
        
    


    @patch('subprocess.run')
    def test_clone_successful(self, mock_subprocess_run):
        # Mock the subprocess.run function to return a successful result
        mock_subprocess_run.return_value.returncode = 0
        mock_subprocess_run.return_value.stdout = b"Cloning into 'destination'..."

        # Call the function with mock data
        result = clone_repository('repo_url', 'destination')

        # Assertions
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"Cloning into 'destination'...")

        # Ensure that subprocess.run was called with the expected arguments
        mock_subprocess_run.assert_called_with(['git', 'clone', 'repo_url', 'destination'],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True

    @patch('subprocess.run')
    def test_clone_failed(self, mock_subprocess_run):
        # Mock the subprocess.run function to return a failed result
        mock_subprocess_run.return_value.returncode = 1
        mock_subprocess_run.return_value.stderr = b"Error: Repository not found"

        # Call the function with mock data
        result = clone_repository('repo_url', 'destination')

        # Assertions
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, b"Error: Repository not found")

        # Ensure that subprocess.run was called with the expected arguments
        mock_subprocess_run.assert_called_with(['git', 'clone', 'repo_url', 'destination'],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return False

    @patch('requests.post')
    def test_create_repo_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_post.return_value.status_code = 201  # HTTP status code for created
        mock_post.return_value.json.return_value = {'name': 'new-repo-name', 'html_url': 'https://github.com/user/new-repo-name'}

        # Call the function with mock data
        response = create_github_repo(github_token, 'new-repo-name', 'mit')

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'name': 'new-repo-name', 'html_url': 'https://github.com/user/new-repo-name'})

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            'https://api.github.com/user/repos',
            headers={
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            },
            json={
                'name': 'new-repo-name',
                'license_template': 'mit',
                'auto_init': True
            }
        )
        return True

    # @patch('requests.delete')
    # def test_delete_repo_success(self, mock_delete):
    #     # Mock the requests.delete method to return a successful response
    #     mock_delete.return_value.status_code = 204  # HTTP status code for successful deletion

    #     # Call the function with mock data
    #     response = delete_github_repo(github_token, 'username', 'repo-to-delete')

    #     # Assertions
    #     self.assertEqual(response.status_code, 204)

    #     # Ensure that requests.delete was called with the expected arguments
    #     mock_delete.assert_called_with(
    #         f'https://api.github.com/repos/username/repo-to-delete',
    #         headers={
    #             'Authorization': f'token  {github_token}',
    #             'Accept': 'application/vnd.github.v3+json'
    #         }
    #     )
    #     return True

    @patch('requests.delete')
    def test_delete_repo_failure(self, mock_delete):
        # Mock the requests.delete method to return a failed response
        mock_delete.return_value.status_code = 404  # Simulate a not found error

        # Call the function with mock data
        response = delete_github_repo(github_token, 'username', 'repo-to-delete')

        # Assertions
        self.assertEqual(response.status_code, 404)

        # Ensure that requests.delete was called with the expected arguments
        mock_delete.assert_called_with(
            f'https://api.github.com/repos/username/repo-to-delete',
            headers={
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            }
        )
        return False

    @patch('requests.post')
    def test_fork_repo_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_post.return_value.status_code = 202  # HTTP status code for accepted (accepted for asynchronous processing)

        # Call the function with mock data
        response = fork_repo('TommasU', 'slash', github_token)

        # Assertions
        self.assertEqual(response.status_code, 202)

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            'https://api.github.com/repos/TommasU/slash/forks',
            headers={
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            }
        )
        return True

    @patch('requests.post')
    def test_fork_repo_failure(self, mock_post):
        # Mock the requests.post method to return a failed response
        mock_post.return_value.status_code = 404  # Simulate a not found error

        # Call the function with mock data
        response = fork_repo('target_user', 'target_repo', github_token)

        # Assertions
        self.assertEqual(response.status_code, 404)

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            f'https://api.github.com/repos/target_user/target_repo/forks',
            headers={
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            }
        )
        return False


if __name__ == '__main__':
    unittest.main()

