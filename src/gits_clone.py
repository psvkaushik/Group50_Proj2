"""
Copyright (C) 2023 G.I.T.S.3 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: gits3.1project@gmail.com

"""

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

