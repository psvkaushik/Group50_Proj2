from flask import Flask, request, render_template

import gits_createrepo 
import gits_delete
import gits_clone
import gits_pull
import gits_fork
import gits_checkbranch


# file_path = r'C:\Users\psvka\OneDrive\Desktop\fall23\CSC519\CSC-519-WS-5\vars.yaml'
# with open(file_path, 'r') as file:
#     data = yaml.safe_load(file)
token = "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"


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('GIITS.html')

@app.route('/create_repo', methods=['POST'])
def create_github_repo():
    # Get the repo name and token from the form
    repo_name = request.form['repoName']
    #token = request.form['token']

    # Call your create_github_repo function from your Python script
    response = gits_createrepo.create_github_repo(token, repo_name)
    print(response)

    # Handle the response as needed (e.g., return a success message)
    if response.status_code == 201:
        return "Repository created successfully!"
    else:
        return f"Error creating repository. Status code: {response.status_code}"

@app.route('/clone_repo', methods=['POST'])
def clone_repository():
    repo_url = request.form['repoURL']
    destination_path = request.form['destinationPath']
    result = gits_clone.clone_repository(repo_url, destination_path)
    if result.returncode == 0:
        return "Repository cloned successfully!"
    else:
        return f"Error cloning repository. Error message: {result.stderr}"

@app.route('/delete_repo', methods=['POST'])
def delete_repository():
    user_name = request.form['userName']
    repo_name = request.form['repoName']
    # Call your delete_repo function here and handle the response
    # For example, you can return a success or error message
    result = gits_delete.delete_github_repo(token,user_name, repo_name)
    if result.status_code == 204:
        return "Repository deleted successfully!"
    else:
        return f"Error deleting repository. Error message: {result.json()}"

@app.route('/fork_repo', methods=['POST'])
def fork_repository():
    user_name = request.form['userName']
    repo_name = request.form['repoName']
    # Call your fork_repo function here and handle the response
    # For example, you can return a success or error message

    result = gits_fork.fork_repo(user_name, repo_name, token)
    if result.returncode == 0:
        return "Repository forked successfully!"
    else:
        return f"Error forking repository. Error message: {result.json()}"

@app.route('/check_branch', methods=['POST'])
def check_branch():
    user_name = request.form['userName']
    repo_name = request.form['repoName']
    branch_name = request.form['branchName']
    # Call your fork_repo function here and handle the response
    # For example, you can return a success or error message
    result = check_branch_exists(token, user_name, repo_name, branch_name)
    if result.status_code == 200:
        return f"Branch {branch_name} in the {repo_name} exists!"
    else:
        return f"Error!! Error message: {result.json()}"

@app.route('/pull_repo', methods=['POST'])
def pull_repository():
    repo_owner = request.form['repoOwner']
    repo_name = request.form['repoName']
    filename = request.form['filename']
    local_filepath = request.form['localPath']
    result = gits_pull.pull_file_from_github(token, repo_owner, repo_name, filename, local_filepath)
    if result.status_code == 200:
        return (f"File '{filename}' successfully pulled to '{local_filepath}'")
    else:
        return (f"Error pulling the file. Status code: {result.status_code}. /n {result.text}")



if __name__ == '__main__':
    app.run(debug= True, port=5020)