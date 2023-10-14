import unittest
from unittest.mock import Mock, patch
from create_repo import create_github_repo
import os
github_token = os.environ['GITS_GITHUB_TOKEN']

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
        
    @patch('requests.get')
    def test_successful_request(self, mock_get):
        # Mock the requests.get method to return a 200 response with content
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Test content'

        # Call the function with mock data
        pull_file_from_github('your_token', 'owner', 'repo', 'file.txt', 'local.txt')

        # Assertions
        mock_get.assert_called_with(
            'https://raw.githubusercontent.com/owner/repo/main/file.txt',
            headers={
                'Authorization': 'token '+ github_token,
                'Accept': 'application/vnd.github.v3.raw'
            }
        )

    @patch('requests.get')
    def test_failed_request(self, mock_get):
        # Mock the requests.get method to return a non-200 response
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = 'Not Found'

        # Call the function with mock data
        pull_file_from_github('your_token', 'owner', 'repo', 'file.txt', 'local.txt')

        # Assertions
        mock_get.assert_called_with(
            'https://raw.githubusercontent.com/owner/repo/main/file.txt',
            headers={
                'Authorization': 'token '+ github_token,
                'Accept': 'application/vnd.github.v3.raw'
            }
        )

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
                'Authorization': github_token,
                'Accept': 'application/vnd.github.v3+json'
            },
            json={
                'name': 'new-repo-name',
                'license_template': 'mit',
                'auto_init': True
            }
        )

    @patch('requests.post')
    def test_create_repo_failure(self, mock_post):
        # Mock the requests.post method to return a failed response
        mock_post.return_value.status_code = 404  # Simulate a not found error

        # Call the function with mock data
        response = create_github_repo(github_token, 'new-repo-name', 'mit')

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), None)  # No JSON response for a failed request

        # Ensure that requests.post was called with the expected arguments
        mock_post.assert_called_with(
            'https://api.github.com/user/repos',
            headers={
                'Authorization': 'token + github_token,
                'Accept': 'application/vnd.github.v3+json'
            },
            json={
                'name': 'new-repo-name',
                'license_template': 'mit',
                'auto_init': True
            }
        )


if __name__ == '__main__':
    unittest.main()
