import requests
import subprocess
from subprocess import PIPE

from read_token import github_token

headers = {
    "Accept" : "application/vnd.github.v3+json",
    "Authorization" : f'token {github_token}'
}

url = "https://github.com/GITSSE23/test"

data = requests.get(url, headers)
print(data)