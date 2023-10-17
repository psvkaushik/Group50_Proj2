import requests

def count_commits_in_github_repo(repo_url): #function to extract the owner and repo name from the GitHub URL
    parts = repo_url.rstrip('/').split('/')
    owner = parts[-2]
    repo_name = parts[-1]

    #commit_count = 0
    #page = 1
    #per_page = 100

    #while True:
    api_url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    #github API endpoint for getting commits
    params = {'page': page, 'per_page': per_page}
    response = requests.get(api_url, params=params) #send a GET request to the GitHub API
    return response
            #response.raise_for_status()  #raise an exception for bad responses
            
            #commits = response.json() #get the JSON response
            #commit_count += len(commits) #add the number of commits on this page to the count
            
            #if len(commits) < per_page: #check if there are more pages to retrieve
            #    break
            #page += 1
            
        #except requests.exceptions.RequestException as e:
            #print(f"Error: {e}")
        #    return None

    #return commit_count

if __name__ == '__main__':
    repo_url = input("Enter the public GitHub repository URL: ")
    commit_count = count_commits_in_github_repo(repo_url)
    
    if commit_count is not None:
        print(f"Number of commits in the repository: {commit_count}")
        
