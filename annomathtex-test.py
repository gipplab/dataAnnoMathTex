#!/usr/bin/env python
# ST2/ST3 compat
from __future__ import print_function
import os
import urllib3
urllib3.disable_warnings()
from github import Github
token = os.getenv('apikey', False)
if not token:
    print('Token not set')
    exit(2)
g = Github(token)
repo = g.get_repo("ag-gipp/dataAnnoMathTex")
user = g.get_user()
print(user.login)
repo.create_file("/test.txt", "pyGit test commit", "This is the content of the test file.")
