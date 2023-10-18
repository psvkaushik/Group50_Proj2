"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import subprocess
from gits_commit import commit

def push(PAT, user_name, dir_path, repo_name, branch='main', file_path='.', commit_msg='user forgot to add message'):
    """
    Function which commits code to local branches
    PAT - The user's PAT token
    dir_path - local directory where the code is stored
    repo_name - name of the repo to which the code is pushed to. 
    branch - if user wants to switch branch, the name of the new branch, 
                default is set to main.
    dir_path - path to where the repo is hosted locally
    commit_msg - The commit message
    files - files the user wants to commit

    make sure the folder name in local matches the repo_name
    """
    
    commit_response = commit(dir_path, branch, file_path, commit_msg)
    
    command = ['git', 'push', f'https://{PAT}@github.com/{user_name}/{repo_name}.git']
    push_response = subprocess.run(command, cwd=dir_path,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return commit_response, push_response