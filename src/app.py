from flask import Flask, request, render_template
import create_repo # Import your Python script
import delete_repo
import clone_repo
import yaml

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
    response = create_repo.create_github_repo(token, repo_name)
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
    result = clone_repo.clone_repository(repo_url, destination_path)
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
    result = delete_repo.delete_github_repo(token,user_name, repo_name)
    if result.status_code == 204:
        return "Repository deleted successfully!"
    else:
        return f"Error deleting repository. Error message: {result.json()}"


if __name__ == '__main__':
    app.run(debug= True, port=5020)