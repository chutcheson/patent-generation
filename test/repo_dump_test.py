import sys
sys.path.append('../src')

from repo_dump import dump_repo_to_text_file

repo_url = "https://github.com/ros-drivers/usb_cam"
dump_repo_to_text_file(repo_url)