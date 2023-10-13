from flask import Flask, request, render_template
import create_repo  # Import your Python script

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('GIITS.html')

@app.route('/create_repo', methods=['POST'])
def create_github_repo():
    # Get the repo name and token from the form
    repo_name = request.form['repoName']
    token = request.form['token']

    # Call your create_github_repo function from your Python script
    response = create_repo.create_github_repo(token, repo_name)

    # Handle the response as needed (e.g., return a success message)
    if response.status_code == 201:
        return "Repository created successfully!"
    else:
        return f"Error creating repository. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug= True, port=5020)
