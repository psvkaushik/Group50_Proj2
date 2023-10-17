# About App.py

This documentation provides an overview of the Flask web application, App.py, which serves as a front-end for various GitHub-related functions. The application allows users to interact with GitHub repositories, including creating, cloning, deleting, forking, checking branches, pulling files, fetching branches, counting commits, merging branches, and viewing commit differences.

## Code Description

The App.py code is organized into several routes, each of which handles a specific GitHub-related action. The following sections describe the routes and their corresponding functions:

### Index Route
- **Route**: `/`
- **Description**: This route renders an HTML template (`GIITS.html`) when the user visits the root URL.

### Create GitHub Repository Route
- **Route**: `/create_repo`
- **Description**: This route allows users to create a new GitHub repository by providing a repository name. It calls the `gits_createrepo.create_github_repo` function and handles the response accordingly.

### Clone GitHub Repository Route
- **Route**: `/clone_repo`
- **Description**: This route allows users to clone an existing GitHub repository by providing the repository URL and destination path. It calls the `gits_clone.clone_repository` function and returns a success or error message based on the result.

### Delete GitHub Repository Route
- **Route**: `/delete_repo`
- **Description**: Users can delete a GitHub repository by providing their GitHub username and the repository name. It calls the `gits_delete.delete_github_repo` function and returns a success or error message based on the result.

### Fork GitHub Repository Route
- **Route**: `/fork_repo`
- **Description**: This route allows users to fork an existing GitHub repository by providing their GitHub username and the repository name. It calls the `gits_fork.fork_repo` function and returns a success or error message based on the result.

### Check Branch Route
- **Route**: `/check_branch`
- **Description**: Users can check if a specific branch exists in a GitHub repository. It calls the `gits_checkbranch.check_branch_exists` function and returns a success or error message based on the result.

### Pull GitHub Repository Route
- **Route**: `/pull_repo`
- **Description**: Users can pull a specific file from a GitHub repository by providing the repository owner, repository name, filename, and local path. It calls the `gits_pull.download_github_repo` function and returns a success or error message based on the result.

### Get Branches Route
- **Route**: `/get_branches`
- **Description**: This route allows users to fetch the branches of a GitHub repository. It calls the `gits_branch.get_github_branches` function and returns a list of branch names or an error message.

### Commit Count Route
- **Route**: `/commit_count`
- **Description**: This route fetches the total number of commits in a GitHub repository by providing the repository URL. It calls the `gits_countcommit.count_commits_in_github_repo` function and returns the commit count.

### Merge Branch Route
- **Route**: `/merge_branch`
- **Description**: Users can merge a specific branch in a GitHub repository by providing the repository owner, repository name, and branch name. It calls the `gits_merge.merge_github_branch` function and returns the result of the merge operation.

### Commit Difference Route
- **Route**: `/commit_diff`
- **Description**: This route allows users to view the differences between commits in a GitHub repository's branch by providing the repository owner, repository name, and branch name. It calls the `gits_diff.get_github_commit_diff` function and returns the commit differences.

## How to Run the Code

To run the Flask app, follow these steps:
Replace the `token` variable with your GitHub Personal Access Token to enable GitHub API interactions.
Run the Flask app with the following command:
`python app.py` or `python3 app.py`
Access the web application by opening a web browser and navigating to `http://localhost:5020/`.

Please note that the application is primarily a front-end for GitHub-related actions and depends on the external Python scripts for interacting with the GitHub API.
Feel free to customize and expand the application as needed for your specific use case.
For any questions or issues, please refer to the repository or contact the developer.

