# RAG Complaint Chatbot

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Project Overview

This repository contains the work for building a **Retrieval-Augmented Generation (RAG) chatbot** using the **CFPB consumer complaint dataset**. The chatbot allows users to ask questions about consumer complaints and receive accurate, context-aware answers, with sources shown for transparency.

The project is organized into **four tasks**:

1. **Exploratory Data Analysis (EDA)**
2. **Text Preparation for Semantic Search (Chunking, Embedding, FAISS Indexing)**
3. **RAG Pipeline Implementation**
4. **Interactive Chat Interface (Gradio)**

---

## Table of Contents

* [Project Overview](#project-overview)
* [Dataset](#dataset)
* [Tasks](#tasks)

  * [Task 1: EDA](#task-1-eda)
  * [Task 2: Text Chunking, Embedding, and FAISS Indexing](#task-2-text-chunking-embedding-and-faiss-indexing)
  * [Task 3: RAG Pipeline](#task-3-rag-pipeline)
  * [Task 4: Interactive Chat Interface](#task-4-interactive-chat-interface)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Results & Deliverables](#results--deliverables)
* [Future Improvements](#future-improvements)

---

## Dataset

We used the **Consumer Financial Protection Bureau (CFPB) complaints dataset**, which contains complaint narratives about financial products and services.

* Total complaints used: **82,164**
* Filtered complaints for key financial products: Credit Cards, Personal Loans, Savings Accounts, etc.
* Cleaned and prepared dataset: `filtered_complaints.csv`

**Source:** [CFPB Consumer Complaints](https://www.consumerfinance.gov/data-research/consumer-complaints/)

---

## Tasks

### Task 1: Exploratory Data Analysis (EDA)

**Objective:** Understand the structure and content of consumer complaints to guide preprocessing and model development.

**Steps Completed:**

* Loaded and inspected complaint dataset (`consumer_complaints.csv`)
* Analyzed narrative lengths (0–6,469 words, mostly short complaints)
* Visualized distribution of complaint lengths (right-skewed)
* Cleaned text: lowercase, removed special characters and boilerplate phrases
* Filtered dataset for relevant financial products

**Deliverables:**

* `filtered_complaints.csv`
* Histogram visualizing narrative lengths
* Task 1 notebook: `notebooks/task1_eda.ipynb`

---

### Task 2: Text Chunking, Embedding, and FAISS Indexing

**Objective:** Convert complaints into a searchable format for semantic retrieval.

**Steps Completed:**

* Sampled ~15,000 complaints to preserve product proportions
* Split long narratives into chunks (with overlap to maintain context)
* Generated embeddings using `SentenceTransformer("all-MiniLM-L6-v2")`
* Built **FAISS vector store** for semantic search
* Stored metadata for each chunk: `complaint_id`, `product`, `chunk_index`, `text`

**Deliverables:**

* Notebook: `notebooks/text_chunking_embedding.ipynb`
* Persisted FAISS vector store: `vector_store/faiss_index.bin`
* Metadata pickle: `vector_store/metadata.pkl`

---

### Task 3: RAG Pipeline

**Objective:** Build the logic for **Retrieval-Augmented Generation** using the FAISS vector store and an answer generator.

**Steps Completed:**

* Implemented `retrieve()` function: fetches top-k relevant chunks from FAISS based on a query
* Implemented `generate_answer()` function: generates answers from retrieved chunks using a model or template-based generation
* Created **pipeline module**: `src/pipeline.py`
* Tested pipeline with sample queries

**Deliverables:**

* Python module: `src/pipeline.py`
* Task 3 notebook: `notebooks/task3_rag_pipeline.ipynb` (used for testing, not required to run app)
* Evaluation table & analysis included in final report

---

### Task 4: Interactive Chat Interface

**Objective:** Build a **user-friendly interface** for non-technical users to interact with the RAG system.

**Steps Completed:**

* Built using **Gradio** (`app.py`)
* Core functionality:

  * Text input box for user queries
  * "Ask" button to submit question
  * Streaming or instant display of generated answer
  * Display sources (retrieved chunks) for transparency
  * "Clear" button to reset conversation
* Tested locally and verified functionality

**Deliverables:**

* `app.py` (Gradio app)
* Screenshots/GIF for report
* Clean UI for easy interaction

**Run locally:**

```bash
# Activate virtual environment
venv\Scripts\Activate.ps1   # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Run Gradio app
python app.py
```

* The app will provide a URL to open in a browser and start chatting with the RAG chatbot.

---

## Project Structure

```
rag-complaint-chatbot/
├── app.py                        # Gradio chat interface
├── filtered_complaints.csv       # Cleaned dataset
├── notebooks/
│   ├── task1_eda.ipynb
│   ├── text_chunking_embedding.ipynb
│   └── task3_rag_pipeline.ipynb
├── src/
│   ├── __init__.py
│   ├── pipeline.py               # RAG pipeline
│   ├── retrieval.py              # Retrieval functions
│   └── generator.py              # Answer generation functions
├── vector_store/
│   ├── faiss_index.bin
│   └── metadata.pkl
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/rag-complaint-chatbot.git
cd rag-complaint-chatbot
```

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

* **Run Task 3 pipeline (optional, testing):**

```python
from src.pipeline import rag_pipeline

query = "What are common issues with credit cards?"
answer, sources = rag_pipeline(query)
print(answer)
print(sources)
```

* **Run interactive chat (Task 4):**

```bash
python app.py
```

---

## Results & Deliverables

* **EDA results**: complaint length histogram, data cleaning insights
* **FAISS vector store**: semantic search enabled on complaint chunks
* **RAG pipeline**: retrieval + generation logic, modularized in `src/`
* **Interactive chatbot**: fully working Gradio app with sources displayed
* **Final report**: evaluation table, pipeline analysis, screenshots

---

## Future Improvements

* Integrate **streaming generation** for token-by-token response
* Use larger/fine-tuned LLMs for improved accuracy
* Add **multi-turn conversation memory**
* Deploy web app to **Heroku / Streamlit Cloud**

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Do you want me to do that next?
