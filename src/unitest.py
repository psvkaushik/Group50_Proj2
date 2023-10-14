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

if __name__ == '__main__':
    unittest.main()

