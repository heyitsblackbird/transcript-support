'''
Retrieval service for fetching relevant chunks based on user queries.
'''

from sentence_transformers import SentenceTransformer
import chromadb

CHROMA_PATH = 'data/chromaDB'
COLLECTION_NAME = 'documents'
_model = SentenceTransformer('all-MiniLM-L6-v2')
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(name=COLLECTION_NAME)

def generate_query_embedding(query:str) -> list:
    '''
    Generate embedding for the user query.
    '''
    return _model.encode(query).tolist()

def retrieve_relevant_chunks(question:str, top_k:int = 5) -> list[dict]:
    '''
    Retrieve relevant chunks from ChromaDB based on the query embedding.
    '''

    query_embedding = generate_query_embedding(question)
    
    results = _collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=['documents', 'metadatas', 'distances']
    )

    retrieved_chunks = []

    documents = results.get('documents', [[]])
    metadatas = results.get('metadatas', [[]])
    distances = results.get('distances', [[]])

    documents = documents[0] if documents else []
    metadatas = metadatas[0] if metadatas else []
    distances = distances[0] if distances else []

    for i in range(len(documents)):
        metadata = metadatas[i]
        distance = distances[i]

        retrieved_chunks.append({
            'text': documents[i],
            'source': metadata.get('source', 'unknown'),
            'chunk_index': metadata.get('chunk_index'),
            'distance': distance,
        })

    return retrieved_chunks