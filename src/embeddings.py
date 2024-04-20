import os
from google.cloud import storage
import pdfplumber
from transformers import GPT2Tokenizer, GPT2Model

# Initialize tokenizer and model for embeddings
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

# Google Cloud Storage setup
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'src/gcloud/application_default_credentials.json'
client = storage.Client(project='chris-bassano')  # Replace 'your-project-name' with your actual project name
bucket = client.get_bucket('patents_json')

# Function to extract text from a single PDF
def extract_text_from_pdf(blob):
    with pdfplumber.open(blob) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text

def generate_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(0)  # Taking the mean of the last hidden state

# Main processing loop
for blob in bucket.list_blobs(prefix='patents_json/'):  # Assuming PDFs are in a folder named 'pdfs'
    if blob.name.endswith('.pdf'):
        blob.download_to_filename('temp.pdf')
        text = extract_text_from_pdf('temp.pdf')
        embeddings = generate_embeddings(text)
        print(f"Embeddings for {blob.name}: {embeddings}")
        os.remove('temp.pdf')  # Clean up temp file