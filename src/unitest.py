import unittest
from unittest.mock import Mock, patch
from create_repo import create_github_repo
class TestCreateGithubRepo(unittest.TestCase):

    @patch('requests.post')
    def test_successful_repo_creation(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        token = 'your_token'
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

        token = 'your_token'
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
                'Authorization': 'token your_token',
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
                'Authorization': 'token your_token',
                'Accept': 'application/vnd.github.v3.raw'
            }
        )


if __name__ == '__main__':
    unittest.main()

