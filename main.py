import requests

import multiprocessing, subprocess, sys

with open('urls.txt','r') as file:
    lines = file.readlines()
for line in lines:
    response = requests.get(line.strip())
    url = response.text.split('download-url')[1].split('href')[1].split('="')[1].split('"')[0]
    subprocess.call(['wget','-P','/home/ubuntu/bucket/', url])
