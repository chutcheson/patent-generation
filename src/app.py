import streamlit as st
import json

from writer import generate_patent
from utils import values_to_markdown

from repo_dump import dump_repo_to_text_file
from disclosure_gen import generate_patent_disclosure

from pathlib import Path

# Assuming these functions are defined elsewhere and imported:
# from your_module import github_to_disclosure, disclosure_to_prior_art, disclosure_and_prior_art_to_patent

def github_to_disclosure(url):

    # default output is at /tmp/git_repo_dump.txt
    #url = "https://github.com/ros-drivers/usb_cam"
    #dump_repo_to_text_file(url)

    # output is /tmp/disclosure.md
    #git_repo_dump_path="/tmp/git_repo_dump.txt"
    #generate_patent_disclosure(git_repo_dump_path)

    # read disclosure
    git_repo_dump_path="/tmp/disclosure.md"
    disclosure_text = Path(git_repo_dump_path).read_text()

    # Dummy function implementation
    return disclosure_text

def disclosure_to_prior_art(disclosure):
    # Dummy function implementation
    return ["Patent 123", "Patent 456"]

def disclosure_and_prior_art_to_patent(disclosure, prior_art):
    # Dummy function implementation
    return "Patent filed for " + disclosure['title']

# Streamlit application starts here
st.title('GitHub to Patent Generator')

github_url = st.text_input("Enter GitHub repository URL:", "")

if github_url:
    disclosure = github_to_disclosure(github_url)
    st.markdown(disclosure)

    st.header("Finding Prior Art")
    prior_art = disclosure_to_prior_art(disclosure)
    st.write("Prior Art Patents:")
    st.write(prior_art)

    st.header("Generating Patent")
    patent_output = generate_patent(disclosure, prior_art)
    patent_markdown = values_to_markdown(patent_output)
    st.markdown(patent_markdown)

