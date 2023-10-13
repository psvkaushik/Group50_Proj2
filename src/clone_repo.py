import subprocess

def clone_repository(repo_url, destinatinon_path):
    """
    Clones the repository to the target destination
    target destination should be an empty directory
    """
    subprocesses = ['git', 'clone', repo_url, destinatinon_path]
    result = subprocess.run(subprocesses, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return result

## return code = 0 -- success
## return code = 128 -- repo doesn't exist or given directory is not empty
# pat = r'C:\Users\psvka\OneDrive\Desktop\fall23\icr'
# print(clone_repository('https://github.com/GITSSE23/ICR', pat))