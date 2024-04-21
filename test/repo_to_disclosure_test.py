import sys
sys.path.append('../src')

from repo_dump import dump_repo_to_text_file
from disclosure_gen import generate_patent_disclosure

# default output is at /tmp/git_repo_dump.txt
repo_url = "https://github.com/ros-drivers/usb_cam"
dump_repo_to_text_file(repo_url)

# output is /tmp/disclosure.md
git_repo_dump_path="/tmp/git_repo_dump.txt"
generate_patent_disclosure(git_repo_dump_path)