import unittest
from unittest.mock import Mock, patch
import subprocess
import json
import requests
from gits_createrepo import create_github_repo
from gits_branch import get_github_branches
from gits_checkbranch import check_branch_exists
from gits_delete import delete_github_repo
from gits_diff import get_github_diff
from gits_fork import fork_repo
from gits_merge import merge_github_branch
from gits_pull import download_github_repo
from gits_countcommit import count_commits_in_github_repo
# from read_token import  username
from gits_clone import clone_repository
from gits_createbranch import create_branch
import app
from flask import Flask

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
            json={
                'name': repo_name,
                'license_template': 'mit',
                'auto_init': True
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
        # self.assertTrue(mock_post.called)
        mock_post.assert_called_once_with(
            f'https://api.github.com/user/repos',
            headers={
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            },
            json={
                'name': repo_name,
                'license_template': 'mit',
                'auto_init': True
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
            "Authorization": f'token your-PAT'
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
        mock_subprocess_run.assert_called_with(['git', 'clone', 'repo_url', 'destination'], stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)

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
        mock_subprocess_run.assert_called_with(['git', 'clone', 'repo_url', 'destination'], stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)

    @patch('gits_delete.requests.delete')
    def test_delete_repo_sucess(self, mock_delete):
        mock_response = Mock()
        mock_response.status_code = 204  # implies successful delete
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
            "Authorization": f'token PAT'
        }

        url = f'https://api.github.com/repos/user_name/repo_name/branches/branch_name'
        # Asserting with mock call
        mock_get.assert_called_once_with(url=url, headers=headers)

    @patch('app.token', 'token')
    @patch('gits_createrepo.create_github_repo')
    def test_app_create_github_repo_success(self, mock_create_github_repo):
        # Configure the mock objects
        mock_create_github_repo.return_value.status_code = 201
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo'}):
            # Call the Flask route function within the request context
            response = app.create_github_repo()

        # Verify the results
        self.assertEqual(response, 'Repository created successfully!')
        mock_create_github_repo.assert_called_with('token', 'my-repo')

    @patch('app.token', 'token')
    @patch('gits_createrepo.create_github_repo')
    def test_app_create_github_repo_failure(self, mock_create_github_repo):
        # Configure the mock objects
        mock_create_github_repo.return_value.status_code = 404
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo'}):
            # Call the Flask route function within the request context
            response = app.create_github_repo()

        # Verify the results
        self.assertEqual(response, "Error creating repository. Status code: 404")
        mock_create_github_repo.assert_called_with('token', 'my-repo')

    @patch('gits_clone.clone_repository')
    def test_app_clone_repository_success(self, mock_clone_repository):
        # Configure the mock objects
        mock_clone_repository.return_value.returncode = 0
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoURL': 'https://github.com/owner/repo', 'destinationPath': '/path/to/clone'}):
            # Call the Flask route function within the request context
            response = app.clone_repository()

        # Verify the results
        self.assertEqual(response, 'Repository cloned successfully!')
        mock_clone_repository.assert_called_with('https://github.com/owner/repo', "/path/to/clone")

    @patch('gits_clone.clone_repository')
    def test_app_clone_repository_failure(self, mock_clone_repository):
        # Configure the mock objects
        mock_clone_repository.return_value.returncode = 1  # Simulate a failed clone
        mock_clone_repository.return_value.stderr = 'Error message for failed clone'
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoURL': 'https://github.com/owner/repo', 'destinationPath': '/path/to/clone'}):
            # Call the Flask route function within the request context
            response = app.clone_repository()

        # Verify the results
        self.assertEqual(response, 'Error cloning repository. Error message: Error message for failed clone')
        mock_clone_repository.assert_called_with('https://github.com/owner/repo', "/path/to/clone")

    @patch('app.token', 'token')
    @patch('gits_delete.delete_github_repo')
    def test_app_delete_github_repo(self, mock_delete_github_repo):
        # Configure the mock objects
        mock_delete_github_repo.return_value.status_code = 204
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo', 'userName': 'userName'}):
            # Call the Flask route function within the request context
            response = app.delete_repository()

        # Verify the results
        self.assertEqual(response, 'Repository deleted successfully!')
        mock_delete_github_repo.assert_called_with('token', "userName", 'my-repo')

    @patch('app.token', 'token')
    @patch('gits_fork.fork_repo')
    def test_app_fork_github_repo(self, mock_fork_github_repo):
        # Configure the mock objects
        mock_fork_github_repo.return_value.status_code = 202
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo', 'userName': 'userName'}):
            # Call the Flask route function within the request context
            response = app.fork_repository()

        # Verify the results
        self.assertEqual(response, 'Repository forked successfully!')
        mock_fork_github_repo.assert_called_with("userName", 'my-repo', 'token')

    @patch('app.token', 'token')
    @patch('gits_checkbranch.check_branch_exists')
    def test_app_check_branch(self, mock_check_branch_github_repo):
        # Configure the mock objects
        mock_check_branch_github_repo.return_value.status_code = 200
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo', 'userName': 'userName', 'branchName': 'my-branch'}):
            # Call the Flask route function within the request context
            response = app.check_branch()

        # Verify the results
        self.assertEqual(response, 'Branch my-branch in the my-repo exists!')
        mock_check_branch_github_repo.assert_called_with('token', "userName", 'my-repo', 'my-branch')

    @patch('app.token', 'token')
    @patch('gits_createbranch.create_branch')
    def test_app_create_branch_exists(self, mock_create_branch_github_repo):
        # Configure the mock objects
        mock_create_branch_github_repo.return_value.status_code = 422
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo', 'userName': 'userName',
                                                                     'baseBranch': 'baseBranch', 'newBranch':
                                                                         'newBranch'}):
            # Call the Flask route function within the request context
            response = app.create_branch()

        # Verify the results
        self.assertEqual(response, 'Branch newBranch in the repo my-repo already exists!')
        mock_create_branch_github_repo.assert_called_with("userName", 'my-repo', 'baseBranch', 'newBranch', 'token')

    @patch('app.token', 'token')
    @patch('gits_createbranch.create_branch')
    def test_app_create_branch_new(self, mock_create_branch_github_repo):
        # Configure the mock objects
        mock_create_branch_github_repo.return_value.status_code = 201
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoName': 'my-repo', 'userName': 'userName',
                                                                     'baseBranch': 'baseBranch', 'newBranch':
                                                                         'newBranch'}):
            # Call the Flask route function within the request context
            response = app.create_branch()

        # Verify the results
        self.assertEqual(response, 'Branch newBranch in the repo my-repo created successfully!')
        mock_create_branch_github_repo.assert_called_with("userName", 'my-repo', 'baseBranch', 'newBranch', 'token')

    @patch('app.token', 'token')
    @patch('gits_pull.download_github_repo')
    def test_app_pull_github_repo(self, mock_pull_github_repo):
        # Configure the mock objects
        mock_pull_github_repo.return_value.status_code = 200
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoOwner': 'repoOwner', 'repoName': 'repoName',
                                                                     'localPath': 'localPath'}):
            # Call the Flask route function within the request context
            response = app.pull_repository()

        # Verify the results
        self.assertEqual(response, "Repository 'repoName' successfully downloaded and extracted to 'localPath'")
        mock_pull_github_repo.assert_called_with( 'token', "repoOwner", 'repoName', 'localPath')

    @patch('app.token', 'token')
    @patch('gits_branch.get_github_branches')
    def test_app_get_branch_github_repo(self, mock_get_branch_github_repo):
        # Configure the mock objects
        mock_get_branch_github_repo.return_value.status_code = 200
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoOwner': 'repoOwner', 'repoName': 'repoName'}):
            # Call the Flask route function within the request context
            response = app.get_branches()

        # Verify the results
        self.assertEqual(response, [])
        mock_get_branch_github_repo.assert_called_with("repoOwner", 'repoName', 'token')

    @patch('gits_countcommit.count_commits_in_github_repo')
    def test_app_commit_count(self, mock_clone_commit_count):
        mock_clone_commit_count.return_value = '100'
        # Configure the mock objects
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoURL': 'https://github.com/owner/repo'}):
            # Call the Flask route function within the request context
            response = app.get_commit_count()

        # Verify the results
        self.assertEqual(response, 'The total number of commits in the given repo is 100')
        mock_clone_commit_count.assert_called_with('https://github.com/owner/repo')

    @patch('app.token', 'token')
    @patch('gits_merge.merge_github_branch')
    def test_app_merge_branch_github_repo(self, mock_merge_branch_github_repo):
        # Configure the mock objects
        mock_merge_branch_github_repo.return_value = "Merged Successfully!"
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoOwner': 'repoOwner', 'repoName': 'repoName',
                                                                     'branchName': 'branchName'}):
            # Call the Flask route function within the request context
            response = app.merge_branch()

        # Verify the results
        self.assertEqual(response, "Merged Successfully!")
        mock_merge_branch_github_repo.assert_called_with("repoOwner", 'repoName', 'branchName', 'token')

    @patch('app.token', 'token')
    @patch('gits_diff.get_github_diff')
    def test_app_diff(self, mock_diff):
        # Configure the mock objects
        mock_diff.return_value = "Message"
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'repoOwner': 'repoOwner', 'repoName': 'repoName',
                                                                     'branchName': 'branchName'}):
            # Call the Flask route function within the request context
            response = app.diff()

        # Verify the results
        self.assertEqual(response, "Message")
        mock_diff.assert_called_with("repoOwner", 'repoName', 'branchName', 'token')

    @patch('app.token', 'token')
    @patch('gits_commit.commit')
    def test_app_commit_diff(self, mock_commit_diff):
        # Configure the mock objects
        mock_commit_diff.return_value = "sample diff!"
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'localPath': 'localPath', 'branchName': 'branchName',
                                                                    'filename': 'filename', 'commit_msg': 'commit_msg'}):
            # Call the Flask route function within the request context
            response = app.commit_diff()

        # Verify the results
        self.assertEqual(response, "sample diff!")
        mock_commit_diff.assert_called_with("localPath", 'branchName', 'filename', 'commit_msg')

    @patch('app.token', 'token')
    @patch('gits_push.push')
    def test_app_push(self, mock_push):
        # Configure the mock objects
        mock_push.return_value = "sample push!"
        test_app = Flask(__name__)

        with test_app.test_request_context('/', method='POST', data={'userName': 'userName', 'localPath': 'localPath',
                                                                     'repoName': 'repoName', 'branchName': 'branchName',
                                                                     'filename': 'filename', 'commit_msg': 'commit_msg'}):
            # Call the Flask route function within the request context
            response = app.push()

        # Verify the results
        self.assertEqual(response, "sample push!")
        mock_push.assert_called_with('token', "userName", "localPath", 'repoName', 'branchName', 'filename', 'commit_msg')
    
    @patch('requests.get')
    def test_count_commits_good(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"sha": "commit1"}, {"sha": "commit2"}]
        mock_get.return_value = mock_response
        repo_url = "https://github.com/owner/repo"
        commit_count = count_commits_in_github_repo(repo_url)
        self.assertEqual(commit_count, "2")

    @patch('requests.get')
    def test_count_commits_request_bad(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Request failed")
        repo_url = "https://github.com/owner/repo"
        commit_count = count_commits_in_github_repo(repo_url)
        self.assertEqual(commit_count, "Error fetching commit count")
    
    @patch('requests.get')
    @patch('requests.post')
    def test_merge_branch_success(self, mock_post, mock_get):
        commit_sha_response = Mock()
        commit_sha_response.status_code = 200
        commit_sha_response.json.return_value = {'object': {'sha': 'commit_sha'}}
        mock_get.return_value = commit_sha_response

        merge_response = Mock()
        merge_response.status_code = 201
        mock_post.return_value = merge_response

        repository_owner = 'owner'
        repository_name = 'repo'
        branch_name = 'test-branch'
        access_token = 'test_access_token'

        result = merge_github_branch(repository_owner, repository_name, branch_name, access_token)

        self.assertEqual(result, "Branch 'test-branch' merged successfully.")

    @patch('requests.get')
    def test_get_commit_sha_failure(self, mock_get):
        commit_sha_response = Mock()
        commit_sha_response.status_code = 404
        commit_sha_response.text = "Commit SHA not found"
        mock_get.return_value = commit_sha_response

        repository_owner = 'owner'
        repository_name = 'repo'
        branch_name = 'test-branch'
        access_token = 'test_access_token'

        result = merge_github_branch(repository_owner, repository_name, branch_name, access_token)
        print(result)
        self.assertEqual(result, "Failed to get the latest commit SHA. Status code: 404\nCommit SHA not found")

    @patch('requests.get')
    @patch('requests.post')
    def test_merge_branch_failure(self, mock_post, mock_get):
        commit_sha_response = Mock()
        commit_sha_response.status_code = 200
        commit_sha_response.json.return_value = {'object': {'sha': 'commit_sha'}}
        mock_get.return_value = commit_sha_response

        merge_response = Mock()
        merge_response.status_code = 400
        merge_response.text = "Merge failed"
        mock_post.return_value = merge_response

        repository_owner = 'owner'
        repository_name = 'repo'
        branch_name = 'test-branch'
        access_token = 'test_access_token'

        result = merge_github_branch(repository_owner, repository_name, branch_name, access_token)

        self.assertEqual(result, "Failed to merge branch 'test-branch'. Status code: 400\nMerge failed")


if __name__ == '__main__':
    unittest.main()
