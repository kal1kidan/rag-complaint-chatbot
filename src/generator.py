def generate_answer(query, retrieved_chunks):
    """
    Generate a response using the retrieved chunks.
    """
    answer = f"Question: {query}\n\n"
    answer += "Based on the complaints, here are the key points:\n"
    
    for i, chunk in enumerate(retrieved_chunks):
        answer += f"{i+1}. [{chunk['product']}] {chunk['text']}\n"
        
    answer += "\nNote: This summary is based only on the retrieved complaints."
    return answer
