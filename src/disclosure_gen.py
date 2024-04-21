import os
import google.generativeai as genai
from pathlib import Path

def disclosure_specification_prompt(repo_data_dump):
    return f"""
    You have been asked to write a patent disclosure for the ideas in the following codebase:

    Codebase:
    {repo_data_dump}

    Select the most interesting idea and generate a patent disclosure such that a compentent pattent attorney can perform a patent search.

    Return your results with a markdown header (e.g. "## Background").
    """

def generator(prompt):
    # Configure the API key and model
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    # Generate content with an extended timeout
    try:
        response = model.generate_content(prompt)
        print("done")
        return response.text
    except google.api_core.exceptions.DeadlineExceeded as e:
        print(f"Request timed out: {e}")
        return None  # or handle the exception as appropriate for your application

def generate_patent_disclosure(git_repo_dump_path="/tmp/git_repo_dump.txt"):

    git_repo_dump_path = "/tmp/git_repo_dump.txt"
    text_data_dump = Path(git_repo_dump_path).read_text()

    prompt = disclosure_specification_prompt(text_data_dump)
    disclosure_text = generator(prompt)

    # repo data dump
    disclosure_path = '/tmp/disclosure.md'
    with open(disclosure_path, "w") as text_file:
        text_file.write(disclosure_text)