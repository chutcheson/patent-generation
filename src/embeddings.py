import os
from google.cloud import storage, aiplatform
import pdfplumber
from transformers import GPT2Tokenizer, GPT2Model

from dotenv import load_dotenv
import csv


# Load environment variables from .env file
load_dotenv()

# Use environment variables
project_id = os.getenv('PROJECT_ID')
project_name = os.getenv('PROJECT_NAME')
location = os.getenv('LOCATION')
index_id = os.getenv('INDEX_ID')
endpoint_display_name = os.getenv('ENDPOINT_DISPLAY_NAME')

# Set path to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Initialize the Vertex AI client
aiplatform.init(project=project_id, location=location)


# Initialize tokenizer and model for embeddings
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

# Google Cloud Storage setup
client = storage.Client(project=project_name)  # Replace 'your-project-name' with your actual project name
bucket = client.get_bucket('patent_bucket_123')  # Replace 'your-bucket-name' with your actual bucket name

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

# Main processing loopu
embedding_data = []  # List to store embedding data

# for blob in bucket.list_blobs(prefix='patents_json/'):  # Assuming PDFs are in a folder named 'pdfs'
#     if blob.name.endswith('.pdf'):
#         blob.download_to_filename('temp.pdf')
#         text = extract_text_from_pdf('temp.pdf')

#         if text:
#             embeddings = generate_embeddings(text)
#             print(f"Embeddings for {blob.name}: {embeddings}")
#             embedding_data.append({"id": os.path.splitext(os.path.basename(blob.name))[0], "embedding": embeddings.tolist()})
#         else:
#             print(f"Empty text for {blob.name}")
        
#         os.remove('temp.pdf')  # Clean up temp file

# Placeholder for embedding CSV file path
embedding_csv_path = 'src/embeddings.csv'

# Write embeddings to CSV file
# with open(embedding_csv_path, 'w', newline='') as csvfile:
#     fieldnames = ['id', 'embedding']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for data in embedding_data:
#         writer.writerow(data)

# Upload CSV file to GCP bucket
# blob = bucket.blob('batch_root/embeddings.csv')
# blob.upload_from_filename(embedding_csv_path)

def query(text):
    # Placeholder for query logic
    embeddings = generate_embeddings(text)
    print(f"Embeddings for query text: {embeddings}")

    # poc return pdf text
    
    return fetch_patent_details_text('US9979873', bucket)
    # return "text sample patent"


def fetch_patent_details_text(patent_id, bucket):
    # Ensure the 'temp' directory exists
    os.makedirs('temp', exist_ok=True)  # This creates the directory if it does not exist and does nothing if it does

    blob_name = f'patents_json/{patent_id}.pdf'
    blob = bucket.blob(blob_name)
    file_path = f'temp/{patent_id}.pdf'

    # Download the PDF file from GCS to the local 'temp' directory
    blob.download_to_filename(file_path)

    # Extract text from the PDF file
    text = extract_text_from_pdf(file_path)

    # Remove the temporary file to clean up
    os.remove(file_path)

    return text

