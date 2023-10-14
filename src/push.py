import subprocess
from check_branch import check_branch_exists

def create_pr(PAT, user_name, repo_name, dir_path,  branch_name='main', file_path='.', commit_message='user forgot to add message'):
    result = []
    check_if_exists = check_branch_exists(PAT, user_name, repo_name, branch_name)
    if check_if_exists.status_code == 200:
        command = ['git', 'checkout', branch_name]
        result.append(subprocess.run(command, cwd=dir_path,  stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    elif check_if_exists.status_code == 404:
        command = ['git', 'checkout', '-b', branch_name]
        result.append(subprocess.run(command, cwd=dir_path,  stdout=subprocess.PIPE, stderr=subprocess.PIPE))

    commands = [
        ['git', 'add', file_path],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push',  f'https://{PAT}@github.com/{user_name}/test2.git']
    ]
   
    for command in commands:
        result.append(subprocess.run(command, cwd=dir_path,  stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    

    return True
