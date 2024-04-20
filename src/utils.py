import os

import google
import google.generativeai as genai

import fitz

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


def convert_pdf_to_text(input_pdf_path, output_pdf_path):
    # Open the provided PDF file
    document = fitz.open(input_pdf_path)

    # Read each page and extract text
    text = ""
    for page in document:
        text += page.get_text()

    # Save the extracted text to a file
    with open(output_pdf_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

    # Close the PDF document
    document.close()

