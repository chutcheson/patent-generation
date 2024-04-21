import os
import google.generativeai as genai
from pathlib import Path

def prior_art_generation_prompt(patent_disclosure_dump):
    return f"""
    You have been asked to generate a list of prior art for the following patent disclosure:

    Patent disclosure:
    {patent_disclosure_dump}

    Generate a list of the most relevant prior art documents and a short summary that should be reviewed to assess the patentability of the invention.

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

def generate_prior_art_list(patent_disclosure_dump_path):

    patent_disclosure_dump = Path(patent_disclosure_dump_path).read_text()

    prompt = prior_art_generation_prompt(patent_disclosure_dump)
    prior_art_text = generator(prompt)

    # repo data dump
    prior_art_path = '/tmp/prior_art.md'
    with open(prior_art_path, "w") as text_file:
        text_file.write(prior_art_text)