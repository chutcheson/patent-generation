import os
from google.cloud import storage
import pdfplumber
from transformers import GPT2Tokenizer, GPT2Model

from dotenv import load_dotenv
import os

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


# Initialize the Vertex AI client
def create_vertex_ai_client(project: str, location: str):
    aiplatform.init(project=project, location=location)
    return aiplatform

# Deploy the index to an endpoint
def deploy_index_to_endpoint(client, index_id: str, endpoint_display_name: str):
    index = client.Index(index_id)
    
    # You might need to specify more configurations based on your needs
    deployed_index = index.deploy(
        deployed_index_display_name=endpoint_display_name,
    )
    
    return deployed_index


# Create a Vertex AI client
client = create_vertex_ai_client(project_id, location)

# Deploy the index to an endpoint and get the deployed index details
deployed_index = deploy_index_to_endpoint(client, index_id, endpoint_display_name)
print(deployed_index)