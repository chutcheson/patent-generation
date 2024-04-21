import sys
sys.path.append('../src')

from prior_art_gen import generate_prior_art_list

patent_disclosure_dump_path="/tmp/git_repo_dump.txt"
generate_prior_art_list(patent_disclosure_dump_path)