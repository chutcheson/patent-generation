from google.cloud import aiplatform

def create_vector_database(project_id, location, display_name):
    client = aiplatform.gapic.FeaturestoreServiceClient(client_options={
        'api_endpoint': f'{location}-aiplatform.googleapis.com'
    })
    parent = f"projects/{project_id}/locations/{location}"
    print(client)
    database = {
        "display_name": display_name,
        "index_config": {
            "dimensions": 128,  # Set the dimension according to your vectors
            "approximate_neighbors_count": 100  # Number of neighbors for ANN search
        }
    }
    operation = client.create_vector_database(parent=parent, vector_database=database)
    print("Waiting for operation to complete...")
    response = operation.result()
    print("Vector database created.")
    return response

def insert_vectors(vector_database_id, vectors):
    client = aiplatform.gapic.VectorDatabaseServiceClient()
    operation = client.batch_insert_vectors(
        parent=vector_database_id,
        vectors=vectors
    )
    print("Inserting vectors...")
    operation.result()
    print("Vectors inserted.")

def search_similar_vectors(vector_database_id, query_vector, k):
    client = aiplatform.gapic.VectorDatabaseServiceClient()
    response = client.search_vectors(
        parent=vector_database_id,
        query_vector=query_vector,
        num_neighbors=k
    )
    print("Search results:")
    for result in response.results:
        print(f"Vector ID: {result.vector_id}, Distance: {result.distance}")

def delete_vector_database(vector_database_id):
    client = aiplatform.gapic.FeaturestoreServiceClient()
    operation = client.delete_vector_database(name=vector_database_id)
    print("Deleting vector database...")
    operation.result()
    print("Vector database deleted.")

# Usage
project_id = 'silver-pad-420918'
location = 'us'
display_name = 'dbms-demo'

# Create a vector database
db_response = create_vector_database(project_id, location, display_name)
vector_database_id = db_response.name

# Assume some vectors for insertion
vectors = [{"vector": list(range(128))} for _ in range(10)]

# Insert vectors into the database
insert_vectors(vector_database_id, vectors)

# Search for similar vectors
search_similar_vectors(vector_database_id, query_vector=list(range(128)), k=5)

# Delete the vector database
delete_vector_database(vector_database_id)


