import os
import glob
import git
from git import Repo  # pip install gitpython
from pathlib import Path

import shutil

def clone_repo(repo_url, local_path):
    try:
        git.Repo.clone_from(repo_url, local_path)
        print(f"Repository cloned successfully to {local_path}")
    except git.exc.GitCommandError as e:
        print(f"Error cloning repository: {e}")

def dump_directory_to_text_file(local_path, text_data_dump_path="/tmp/git_repo_dump.txt"):
    
    initial_paths = glob.glob(local_path + '/**',  recursive = True) 
    file_paths = []
    text_data_dump = ""
    for file_path in initial_paths:
        if not os.path.isdir(file_path):
            file_paths.append(file_path)
            #print(file_path)

            try:
                txt = Path(file_path).read_text()
                text_data_dump = text_data_dump + '\n\n\n\nFile Path: ' + file_path + '\n---------------------\n\n'
                text_data_dump = text_data_dump + txt
            except:
                print("NON TEXT DATA")
                pass # Fond non-text data

    # repo data dump
    with open(text_data_dump_path, "w") as text_file:
        text_file.write(text_data_dump)

def dump_repo_to_text_file(repo_url, local_path = "/tmp/git_repo"):

    # 
    #repo_url = "https://github.com/ros-drivers/usb_cam"
    #local_path = "/tmp/git_repo"

    # delete old repo data
    if os.path.exists(local_path):
        shutil.rmtree(local_path)

    # clone repo to  temp directory
    clone_repo(repo_url, local_path)

    # dump to text file
    dump_directory_to_text_file(local_path, text_data_dump_path="/tmp/git_repo_dump.txt")