# app.py
import gradio as gr
from src.pipeline import rag_pipeline

def ask_question(user_input):
    """
    Function called when user submits a query.
    Returns answer + sources for display.
    """
    retrieved_chunks = rag_pipeline(user_input, top_k=5)
    
    # Format answer and sources separately
    answer_text = "Based on the complaints, here are the key points:\n"
    sources_text = ""
    
    for i, chunk in enumerate(retrieved_chunks):
        answer_text += f"{i+1}. [{chunk['product']}] {chunk['text']}\n"
        sources_text += f"{i+1}. Product: {chunk['product']}, Complaint ID: {chunk['complaint_id']}\n"

    return answer_text, sources_text

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## CrediTrust Complaint RAG Chatbot")
    
    with gr.Row():
        question_input = gr.Textbox(label="Ask a question about complaints")
        submit_btn = gr.Button("Ask")
    
    with gr.Row():
        answer_output = gr.Textbox(label="Answer", lines=10)
        sources_output = gr.Textbox(label="Sources", lines=10)
    
    submit_btn.click(fn=ask_question, inputs=question_input, outputs=[answer_output, sources_output])
    
    clear_btn = gr.Button("Clear")
    clear_btn.click(fn=lambda: ("", ""), inputs=None, outputs=[answer_output, sources_output])

# Run app
if __name__ == "__main__":
    demo.launch()
