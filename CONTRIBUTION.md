# Contributing to GITS3.1 - Sometimes all you need to do is make a REQUEST!!!!

Thank you so much for taking an interest in contributing! There are many ways to contribute to this project.

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct (CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Pull Request Process

1. Maintain GITS3.1 project quality.
2. Should have appropriate ISSUE linked with the Pull request.
3. The PR should be assigned to the individual requesting a merge.
4. The Reviewers must approve the pull request before merging the code.
5. The description should be updated as to what has been asked in the issue.
6. All the development code should accompany unit test cases to support the validation results.
7. The development code should be style checked, well-formatted and syntax error free. Use of pep8, autoflake8 and flake8 tools will enable the users to get the required code quality.
8. Commit messages should company details of the changes been made.

## Bug Reporting Process

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.

Explain the problem and include additional details to help maintainers reproduce the problem:

1. Before raising a GitHub issue, make sure that you are running the latest version of the application and have all recommended OS updates / patches installed
2. Use a clear and descriptive title for the issue to identify the problem.
3. Describe the exact steps which reproduce the problem in as many details as possible. For example, start by explaining how you started Atom, e.g. which command exactly you used in the terminal, or how you started Atom otherwise. When listing steps, don't just say what you did, but explain how you did it. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut or an Atom command, and if so which one?
4. Provide specific examples to demonstrate the steps. Include links to files or GitHub projects, or copy/paste-able snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
5. Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
6. Explain which behavior you expected to see instead and why.
7. Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem.

## Enhancement suggestion process / Feature request Process

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.

1. Use a clear and descriptive title for the issue to identify the suggestion.
2. Provide a step-by-step description of the suggested enhancement in as many details as possible.
3. Provide specific examples to demonstrate the steps.
4. Describe the current behavior and explain which behavior you expected to see instead and why.
5. Explain why this enhancement would be useful to most users and isn't something that can or should be implemented as a community package.


# Contributing to GITS Homepage

Thank you for considering contributing to the GITS Homepage project. Your contributions help make this project better. This document provides guidelines on how to add further functionality to the existing HTML script.

## Table of Contents

- [Getting Started](#getting-started)
- [Contributing Guidelines](#contributing-guidelines)
- [Adding New Functionality](#adding-new-functionality)
- [Testing](#testing)
- [Submitting a Pull Request](#submitting-a-pull-request)

## Getting Started

Before you start contributing, please make sure you have the following prerequisites:

1. A basic understanding of HTML and JavaScript.
2. A basic understanding of Python and Flask framework.
3. A local development environment set up.

## Contributing Guidelines

To ensure a smooth and efficient contribution process, please follow these guidelines:

- Fork the [GITS Homepage repository](https://github.com/your-username/gits-homepage) on GitHub to your own account.
- Clone your fork to your local development environment:

```bash
git clone https://github.com/your-username/gits-homepage.git
cd gits-homepage


1. Create a new file in _PROJECT HOME_/src/gits\_<command name>.py
2. Follow the template below to create a new command and update the values in

   ```python
   import requests

   def func(owner, repo, branch, github_token):
       try:
           # Define the API URL or additional parameters here.
           url = "  "
           # Set up the request headers with the provided GitHub token for authentication.
           headers = {
               'Authorization': f'token {github_token}',
           }

           # Send an HTTP request to the GitHub API and process the response.

           # You can insert the logic to perform specific GitHub actions here.
           # For example, getting the latest commit SHA or comparing branches.

       except Exception as e:
           print("ERROR: An exception occurred")
           print("ERROR: {}".format(str(e)))
           return False

       return True

   if __name__ == "__main__":
       owner = 'YourGitHubUsername'  # Replace with your GitHub username or organization name.
       repo = 'YourRepositoryName'  # Replace with the name of the GitHub repository.
       branch = 'main'  # Specify the branch or additional parameters needed.
       github_token = 'YourGitHubToken'  # Replace with your GitHub personal access token.

       func(owner, repo, branch, github_token)

   ```

3. Add the following entries in _PROJECT HOME_/code/gits.py ==> HTML
