import sys
sys.path.append('../src')

from disclosure_gen import generate_patent_disclosure

git_repo_dump_path="/tmp/git_repo_dump.txt"
generate_patent_disclosure(git_repo_dump_path)