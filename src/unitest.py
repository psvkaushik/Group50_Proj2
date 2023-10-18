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
from gits_createbranch import create_branch

import os
# github_token = os.environ["GITS_GITHUB_TOKEN"]
# github_username = os.environ["GITS_USERNAME"]

github_token = "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"
username = 'GITSSE23'

class Test(unittest.TestCase):

    @patch('gits_createrepo.requests.post')
    def test_successful_repo_creation(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        token = 'github_token'
        repo_name = 'test_repo'

        # Act
        response = create_github_repo(token, repo_name)
        self.assertEqual(response.status_code, 201)
        mock_post.assert_called_once_with(
            f'https://api.github.com/user/repos',
            headers={
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            },
            json = {
        'name': repo_name,
        'license_template': 'mit',
        'auto_init': True  # This will initialize the repository with a README.
    }
        )

    @patch('gits_createrepo.requests.post')
    def test_failed_repo_creation(self, mock_post):
        # Create a mock response
        mock_response = Mock()
        mock_response.status_code = 422  # Simulating an error status code
        mock_response.json.return_value = {'message': 'Repository already exists'}
        mock_post.return_value = mock_response

        token = 'github_token'
        repo_name = 'test_repo'

        # Act
        response = create_github_repo(token, repo_name)

        # Assert
        self.assertEqual(response.status_code, 422)
        #self.assertTrue(mock_post.called)
        mock_post.assert_called_once_with(
            f'https://api.github.com/user/repos',
            headers={
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            },
            json = {
        'name': repo_name,
        'license_template': 'mit',
        'auto_init': True  # This will initialize the repository with a README.
    }
        )
        

    @patch('gits_createbranch.check_branch_exists')
    @patch('gits_createbranch.requests.post')
    @patch('gits_createbranch.requests.get')
    def test_create_branch_success(self, mock_get, mock_post, mock_check_branch_exists):
        # Mock the response of the method check_branch_exists
        mock_check_branch_exists.return_value.status_code = 200

        # Mock the response of a get request 
        mock_get.return_value.json.return_value = {'commit': {'sha': 'abcdef1234567890'}}

        # Mock the response of post request
        mock_post.return_value.status_code = 201

        # Call the function with mock values
        result = create_branch('user', 'repo', 'main', 'feature', 'your-PAT')
        headers = {
        "Accept": 'application/vnd.github.v3+json',
        "Authorization" : f'token your-PAT'
    }
        data = {
            "ref": f"refs/heads/feature",
            "sha": 'abcdef1234567890'
        }

        # Assert that the expected calls were made, this follows the same order in the gits_createbranch.py
        mock_check_branch_exists.assert_called_once_with('your-PAT', 'user', 'repo', 'main')
        mock_get.assert_called_once_with('https://api.github.com/repos/user/repo/branches/main', headers=headers)
        mock_post.assert_called_once_with('https://api.github.com/repos/user/repo/git/refs', headers=headers, json=data)

        # Assert the result
        self.assertEqual(result.status_code, 201)

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



    @patch('gits_delete.requests.delete')
    def test_delete_repo_sucess(self, mock_delete):
        
        mock_response = Mock()
        mock_response.status_code = 204 # implies successful delete
        mock_delete.return_value = mock_response 

        # Call the function with mock data
        response = delete_github_repo('github_token', 'user', 'test_repo')


        # Assertions
        self.assertEqual(response.status_code, 204)

        # Ensure that requests.delete was called with the expected arguments
        mock_delete.assert_called_once_with(
            f'https://api.github.com/repos/user/test_repo',
            headers={
                'Authorization': f'token github_token',
                'Accept': 'application/vnd.github.v3+json'
            }
        )

    @patch('requests.delete')
    def test_delete_repo_failure(self, mock_delete):
        # Mock the requests.delete method to return a failed response
        mock_delete.return_value.status_code = 404  # Simulate a not found error

        # Call the function with mock data
        response = delete_github_repo('github_token', 'username', 'repo-to-delete')

        # Assertions
        self.assertEqual(response.status_code, 404)

        # Ensure that requests.delete was called with the expected arguments
        mock_delete.assert_called_with(
            f'https://api.github.com/repos/username/repo-to-delete',
            headers={
                'Authorization': f'token github_token',
                'Accept': 'application/vnd.github.v3+json'
            }
        )

    @patch('requests.post')
    def test_fork_repo_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_post.return_value.status_code = 202  # HTTP status code for accepted (accepted for asynchronous processing)

        # Call the function with mock data
        response = fork_repo('TommasU', 'slash', 'github_token')

        # Assertions
        self.assertEqual(response.status_code, 202)

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            'https://api.github.com/repos/TommasU/slash/forks',
            headers={
                'Authorization': f'token github_token',
                'Accept': 'application/vnd.github.v3+json'
            }
        )

    @patch('requests.post')
    def test_fork_repo_failure(self, mock_post):
        # Mock the requests.post method to return a failed response
        mock_post.return_value.status_code = 404  # Simulate a not found error

        # Call the function with mock data
        response = fork_repo('target_user', 'target_repo', 'github_token')

        # Assertions
        self.assertEqual(response.status_code, 404)

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            f'https://api.github.com/repos/target_user/target_repo/forks',
            headers={
                'Authorization': f'token github_token',
                'Accept': 'application/vnd.github.v3+json'
            }
        )

    @patch('gits_checkbranch.requests.get')
    def test_checkbranch_success(self, mock_get):
        # mocking the get response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        # using actual function on mock values
        response = check_branch_exists('PAT', 'user_name', 'repo_name', 'branch_name')
        self.assertEqual(response.status_code, 200)

        headers = {
        "Accept": 'application/vnd.github.v3+json',
        "Authorization" : f'token PAT'
    }

        url = f'https://api.github.com/repos/user_name/repo_name/branches/branch_name'
        # Asserting with mock call
        mock_get.assert_called_once_with(url=url, headers=headers)


    



if __name__ == '__main__':
    unittest.main()

