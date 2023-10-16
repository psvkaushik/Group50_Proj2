import subprocess

def clone_repository(repo_url, destinatinon_path):
    """
    Clones the repository to the target destination
    destination_path : target destination - should be an empty directory
    repo_url : the repo which is to be cloned

    """
    subprocesses = ['git', 'clone', repo_url, destinatinon_path]
    result = subprocess.run(subprocesses, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return result

