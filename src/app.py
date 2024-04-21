import streamlit as st
import json

from writer import generate_patent
from utils import values_to_markdown

from repo_dump import dump_repo_to_text_file
from disclosure_gen import generate_patent_disclosure
from prior_art_gen import generate_prior_art_list

from pathlib import Path

# Assuming these functions are defined elsewhere and imported:
# from your_module import github_to_disclosure, disclosure_to_prior_art, disclosure_and_prior_art_to_patent

def github_to_disclosure(url):

    # default output is at /tmp/git_repo_dump.txt
    #url = "https://github.com/ros-drivers/usb_cam"
    dump_repo_to_text_file(url)

    # output is /tmp/disclosure.md
    git_repo_dump_path="/tmp/git_repo_dump.txt"
    generate_patent_disclosure(git_repo_dump_path)

    # read disclosure
    disclosure_dump_path="/tmp/disclosure.md"
    disclosure_text = Path(disclosure_dump_path).read_text()

    # Dummy function implementation
    return disclosure_text

def disclosure_to_prior_art(disclosure_dump_path="/tmp/disclosure.md"):

    generate_prior_art_list(disclosure_dump_path)

    prior_art_path="/tmp/prior_art.md"
    prior_art_text = Path(prior_art_path).read_text()

    # Dummy function implementation
    return prior_art_text

def disclosure_and_prior_art_to_patent(disclosure, prior_art):
    # Dummy function implementation
    return "Patent filed for " + disclosure['title']

# Streamlit application starts here
st.set_page_config(layout="wide")
st.title('GitHub to Patent Generator')

github_url = st.text_input("Enter GitHub repository URL:", "")

# style_text = """
#     <style>
#     .bordered-column {
#         border: 2px solid black;  /* Customize border style as needed */
#         padding: 10px;           /* Optional: Add padding for visual spacing */
#     }
#     </style>
#     """

# Create three columns
col1, col2, col3 = st.columns([1,1,1])

if github_url:
    col1.header("Invention Disclosure")
    disclosure = github_to_disclosure(github_url)
    #col1.markdown(style_text +'<div class="bordered-column">' + disclosure + '</div>')
    col1.markdown(disclosure)

    col2.header("Finding Prior Art")
    disclosure_dump_path="/tmp/disclosure.md"
    prior_art = disclosure_to_prior_art(disclosure_dump_path)
    col2.write("Prior Art Patents:")
    col2.write(prior_art)

    col3.header("Generating Patent")
    patent_output = generate_patent(disclosure, prior_art)
    patent_markdown = values_to_markdown(patent_output)
    col3.markdown(patent_markdown)

