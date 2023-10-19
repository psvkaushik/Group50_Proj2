"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com
"""

import subprocess
from gits_commit import commit

def push(github_token, user_name, dir_path, repo_name, branch='main', files='.', commit_msg='user forgot to add message'):
    """
    Function which commits code to local branches
    github_token - The user's PAT token
    dir_path - local directory where the code is stored
    repo_name - name of the repo to which the code is pushed to. 
    branch - if user wants to switch branch, the name of the new branch, 
                default is set to main.
    dir_path - path to where the repo is hosted locally
    commit_msg - The commit message
    files - files the user wants to commit, separated by spaces

    make sure the folder name in local matches the repo_name
    """
    
    commit_response = commit(dir_path, branch, files, commit_msg)
    
    command = ['git', 'push', f'https://{github_token}@github.com/{user_name}/{repo_name}.git']
    push_response = subprocess.run(command, cwd=dir_path,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return push_response
