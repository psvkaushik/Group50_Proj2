"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

import subprocess

def commit(dir_path, branch = 'main', files = '.', commit_msg = 'commiting through UI'):
    """
    Function which commits code to local branches
    branch - if user wants to switch branch, the name of the new branch, 
                default is set to main.
    dir_path - path to where the repo is hosted locally
    commit_msg - The commit message
    files - files the user wants to commit, separated by spaces
    """
    command = ['git', 'checkout', branch]
    result = subprocess.run(command,  cwd=dir_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 1:
        command = ['git', 'checkout', '-b', branch]
        result = subprocess.run(command, cwd=dir_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command = ['git', 'add', files]
    result = subprocess.run(command, cwd=dir_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command = ['git', 'commit', '-m', commit_msg]
    result = subprocess.run(command, cwd=dir_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result
