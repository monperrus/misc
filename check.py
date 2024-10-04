#!/usr/bin/python3

import json
import requests
import os

# update local files to this repo:
def update_files():
    for x in ["/home/martin/bin/preprocess-latex.py"]:
        os.system("cp "+x+" .")
        


# for all files in the current folder, check that the filename is in README.md
def check_files_in_readme():
    # get the list of files in the current folder
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # read the content of the README.md
    with open('README.md', 'r') as file:
        readme_content = file.read()
    # check if each file is mentioned in the README.md
    for file in files:
        if file not in readme_content:
            # print(f"File '{file}' is not mentioned in the README.md")
            print(f"* [{file}](https://github.com/monperrus/crypto/blob/main/{file})")

update_files()
check_files_in_readme()
