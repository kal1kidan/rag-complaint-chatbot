import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("notebooks/vector_store/faiss_index.bin")

# Load metadata
with open("notebooks/vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, top_k=5):
    """
    Retrieve top_k chunks relevant to the query.
    """
    query_vec = embedder.encode([query])
    distances, indices = index.search(query_vec, top_k)
    
    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx])
    return results
