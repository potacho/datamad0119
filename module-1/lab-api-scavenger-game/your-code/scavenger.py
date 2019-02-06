from dotenv import load_dotenv
import os
import json
import requests
import pandas as pd

# KEY
load_dotenv(dotenv_path='../.env')
SECRET_KEY = os.getenv("KEY")

#Challenge 1
source = "https://api.github.com/repos/ironhack-datalabs/datamad0119/forks"
forks = requests.get(source)
json_forks = forks.json()
#print(json_forks)
languages = list(map(lambda x: {"language":x["language"]}, json_forks))
langs = list({v["language"]:v for v in languages}.values())
print(langs)

#Challenge 2
source = "https://api.github.com/repos/ironhack-datalabs/datamad0119/stats/participation"
commits = requests.get(source)
json_commits = commits.json()
#print(json_commits)
commits = json_commits["all"]
commit_count = sum(commits)
print(type(commits))
print(commit_count)

#Challenge 3