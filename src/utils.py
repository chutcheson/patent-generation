import google.generativeai as genai
import os

import fitz

def generator(prompt):

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def convert_pdf_to_text(pdf_path):
    # Open the provided PDF file
    document = fitz.open(pdf_path)

    # Read each page and extract text
    text = ""
    for page in document:
        text += page.get_text()

    # Save the extracted text to a file
    with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)

    # Close the PDF document
    document.close()

    return "extracted_text.txt"
