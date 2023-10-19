# Contributing to GITS3.1 - Sometimes all you need to do is make a REQUEST!!!!

Thank you so much for taking an interest in contributing! There are many ways to contribute to this project.

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct (CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Contributing Guidelines](#contributing-guidelines)
- [Adding New Functionality](#adding-new-functionality)
- [Testing](#testing)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Template on how to contribute](#Template-on-how-to-contribute)
- [Bug Reporting Process](#Bug-Reporting-Process)
- [Enhancement suggestion process](#Enhancement-suggestion-process)

## Getting Started

Before you start contributing, please make sure you have the following prerequisites:

1. A basic understanding of HTML and JavaScript.
2. A basic understanding of Python and Flask framework.
3. A local development environment set up.

## Contributing Guidelines

1. Maintain GITS3.1 project quality.
2. Should have appropriate ISSUE linked with the Pull request.
3. The PR should be assigned to the individual requesting a merge.
4. The Reviewers must approve the pull request before merging the code.
5. The description should be updated as to what has been asked in the issue.
6. All the development code should accompany unit test cases to support the validation results.
7. The development code should be style checked, well-formatted and syntax error free. Use of pep8, autoflake8 and flake8 tools will enable the users to get the required code quality.
8. Commit messages should company details of the changes been made.

To ensure a smooth and efficient contribution process, please follow these guidelines:

- Fork the [GITS Homepage repository](https://github.com/psvkaushik/Group50_Proj2) on GitHub to your own account.
- Clone your fork to your local development environment:

```bash
git clone https://github.com/psvkaushik/Group50_Proj2
cd Group50_Proj2
```

- Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

- Make your changes to the HTML file as needed.
- Add and commit your changes:

```bash
git add .
git commit -m "Added feature: your-feature-name"
```

## Adding New Functionality

The GITS Homepage provides a dynamic form for different GitHub actions. If you want to add new functionality to this HTML script, follow these steps:

- Open the files in your favorite code editor.
- Add a new section for your feature, including HTML elements for input and a form to submit data.
- Implement the JavaScript function for your new feature. You can use the existing JavaScript code as a reference.
- Implement the function in the backend and also link it to the frontend using the flask [app](/src/app.py)
- Make sure to include proper validation and error handling for user inputs.
- Test your new feature locally to ensure it works as expected.

## Testing

Before you submit a pull request, it's essential to test your changes thoroughly. You can test your new feature by following these steps:

1. Run the GITS Homepage locally using a web server:

```bash
python app.py
```

2. Open your web browser and access the GITS Homepage at http://localhost:5020 (or another port if specified).

3. Test the new functionality by selecting the corresponding option in the dropdown menu and filling out the form. Ensure it works as expected and handles errors gracefully.

4. If you encounter issues or errors, make the necessary adjustments and retest.

## Submitting a Pull Request

Once you have completed your changes and testing, follow these steps to submit a pull request:

- Commit your final changes:

```bash
git add .
git commit -m "Finalizing feature: your-feature-name"
```

- Push your changes to your fork on GitHub:

```bash
git push origin feature/your-feature-name
```

- Visit your fork on GitHub and create a new pull request.
- Provide a clear and concise description of your changes in the pull request.
- Ensure that your pull request is linked to any relevant issues if applicable.
- The maintainers of the GITS Homepage project will review your pull request, provide feedback, and merge it if it meets the project's guidelines.

Thank you for your contribution to the GITS Homepage project! Your help is greatly appreciated.

## Template on how to contribute

1. Create a new file in _PROJECT HOME_/src/gits\_<command name>.py
2. Follow the template below to create a new command and link it to the front-end.

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

3. Add the following entries in ==> HTML

   ```html
   <style>
     #form-container-YourFunctionName {
       display: none;
     }
   </style>

   <select id="option" onchange="toggleForm(this)">
     <option value="YourFunctionRoute">YourOptionName</option>

     <div id="form-container-YourFunctionName">
       <form action="/YourFunctionRoute" method="post">
         <label for="YourInput1">Input 1:</label>
         <input type="text" id="YourInput1" name="YourInput1" required /> <br />
         <br />
         .. ..
         <input type="submit" value="Submit" />
       </form>
     </div>

     <script>
       function toggleForm(selectElement) {
         document.getElementById('form-container-YourFunctionName').style.display = 'none';

         if (selectElement.value === 'YourFunctionRoute') {
           document.getElementById('form-container-YourFunctionName').style.display = 'block';
     </script>
   </select>
   ```

4. Add the route to the flask [app](/src/app.py) as follows:

   ```python
   import func
   @app.route('/YourFunctionRoute', methods=['POST'])
   def function():
   # Perform whatever processing you need to perform and return the data to be displayed
    your_input = request.form['YourInput1']
    response = func(token, your_input)
    return response

   ```

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
