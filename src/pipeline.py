from retrieval import retrieve
from generator import generate_answer

def rag_pipeline(query, top_k=5):
    chunks = retrieve(query, top_k)
    answer = generate_answer(query, chunks)
    return answer
