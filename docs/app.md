# About App.py

This documentation provides an overview of the Flask web application, App.py, which serves as a front-end for various GitHub-related functions. The application allows users to interact with GitHub repositories, including creating, cloning, deleting, forking, checking branches, pulling files, fetching branches, counting commits, merging branches, and viewing commit differences.

## Code Description

The App.py [code](/src/app.py) is organized into several routes, each of which handles a specific GitHub-related action. The following sections describe the routes and their corresponding functions:

### Index Route

- **Route**: `/`
- **Description**: This route renders an [HTML](/src/templates/GIITS.html) template (`GIITS.html`) when the user visits the root URL.

### Create GitHub Repository Route

- **Route**: `/create_repo`
- **Description**: This route allows users to create a new GitHub repository by providing a repository name. It calls the `create_github_repo` function from this [library](/src/gits_createrepo.py) and handles the response accordingly.

### Clone GitHub Repository Route

- **Route**: `/clone_repo`
- **Description**: This route allows users to clone an existing GitHub repository by providing the repository URL and destination path. It calls the `clone_repository` function from this [library](/src/gits_clone.py) and returns a success or error message based on the result.

### Delete GitHub Repository Route

- **Route**: `/delete_repo`
- **Description**: Users can delete a GitHub repository by providing their GitHub username and the repository name. It calls the `delete_github_repo` function from this [library](/src/gits_delete.py) and returns a success or error message based on the result.

### Fork GitHub Repository Route

- **Route**: `/fork_repo`
- **Description**: This route allows users to fork an existing GitHub repository by providing their GitHub username and the repository name. It calls the `fork_repo` function from this [library](/src/gits_fork.py) and returns a success or error message based on the result.

### Check Branch Route

- **Route**: `/check_branch`
- **Description**: Users can check if a specific branch exists in a GitHub repository. It calls the `check_branch_exists` function from this [library](/src/gits_checkbranch.py) and returns a success or error message based on the result.

### Create Branch Route

- **Route**: `/create_branch`
- **Description**: This route allows users to create a new branch in a GitHub repository by providing their GitHub username, repository name, the base branch (from which the new branch will be created), and the name of the new branch. It calls the `create_branch` function from the `gits_createbranch` library and returns a success or error message based on the result.

### Get Branches Route

- **Route**: `/get_branches`
- **Description**: This route allows users to fetch the branches of a GitHub repository. It calls the `get_github_branches` function from this [library](/src/gits_branch.py) and returns a list of branch names or an error message.

### Commit Count Route

- **Route**: `/commit_count`
- **Description**: This route fetches the total number of commits in a GitHub repository by providing the repository URL. It calls the `count_commits_in_github_repo` function from this [library](/src/gits_countcommit.py) and returns the commit count.

### Merge Branch Route

- **Route**: `/merge_branch`
- **Description**: Users can merge a specific branch in a GitHub repository by providing the repository owner, repository name, and branch name. It calls the `merge_github_branch` function from this [library](/src/gits_merge.py) and returns the result of the merge operation.

### Commit Route

- **Route**: `/commit_diff`
- **Description**: Users can commit changes to a specific branch in a GitHub repository. This route takes the local path, branch name, filename, and commit message as input. It calls the `commit` function from the `gits_commit` library and returns the result of the commit operation.

### Push Route

- **Route**: `/push`
- **Description**: This route allows users to push changes to a specific branch in a GitHub repository. Users need to provide their GitHub username, local path, repository name, branch name, filename, and commit message. It calls the `push` function from the `gits_push` library and returns the result of the push operation.

### Difference Route

- **Route**: `/diff`
- **Description**: This route allows users to view the differences between commits in a GitHub repository's branch by providing the repository owner, repository name, and branch name. It calls the `get_github_commit_diff` function from this [library](/src/gits_diff.py) and returns the commit differences.

## How to Run the Code

To run the Flask app, follow these steps:
Replace the `token` variable with your GitHub Personal Access Token to enable GitHub API interactions.
Run the Flask app with the following command:

```
$ python app.py
```

Access the web application by opening a web browser and navigating to `http://localhost:5020/`.

Please note that the application is primarily a front-end for GitHub-related actions and depends on the external Python scripts for interacting with the GitHub API.
Feel free to customize and expand the application as needed for your specific use case.
For any questions or issues, please refer to the repository or contact the developer.
