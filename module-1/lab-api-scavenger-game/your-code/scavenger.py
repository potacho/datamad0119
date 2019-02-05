from dotenv import load_dotenv
import os
import json
import requests
import pandas as pd

# KEY
load_dotenv(dotenv_path='../.env')
SECRET_KEY = os.getenv("KEY")

source = "https://github.com/ironhack-datalabs/mad-oct-2018/forks"
labs = requests.get(source)
datos = labs.json()

#forks = datos["forks_count"]

#forks = list(set([key for keys in datos for key in datos]))
print(datos)
