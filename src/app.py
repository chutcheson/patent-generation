import streamlit as st
import json

from writer import generate_patent
from utils import values_to_markdown

# Assuming these functions are defined elsewhere and imported:
# from your_module import github_to_disclosure, disclosure_to_prior_art, disclosure_and_prior_art_to_patent

def github_to_disclosure(url):
    # Dummy function implementation
    return {"title": "New AI Technique", "description": "A novel approach to AI"}

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
    st.json(disclosure)

    st.header("Finding Prior Art")
    prior_art = disclosure_to_prior_art(disclosure)
    st.write("Prior Art Patents:")
    st.write(prior_art)

    st.header("Generating Patent")
    patent_output = generate_patent(disclosure, prior_art)
    patent_markdown = values_to_markdown(patent_output)
    st.markdown(patent_markdown)

