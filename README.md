# 🧠 RAG Complaint Chatbot

**Intelligent Complaint Analysis for Financial Services**

This repository contains the implementation of a **Retrieval-Augmented Generation (RAG)** system built using **CFPB consumer complaint data**.
The project transforms raw, unstructured customer complaints into **searchable, evidence-backed insights** for internal teams such as Product, Support, and Compliance.

This work is part of **10 Academy – AI Mastery (Week 7 Challenge)**.

---

## 📌 Project Overview

CrediTrust Financial receives thousands of complaints each month across multiple financial products.
Manual analysis is slow, inconsistent, and does not scale.

This project addresses that challenge by:

* Enabling **semantic search** over complaint narratives
* Retrieving the most relevant complaint excerpts using vector similarity
* Generating **grounded answers** with an LLM using retrieved evidence
* Displaying **sources** to increase transparency and trust

---

## 🗂 Repository Structure

```
rag-complaint-chatbot/
├── data/
│   ├── raw/
│   └── processed/
├── vector_store/                # Persisted FAISS index
├── notebooks/                   # EDA & experimentation
│   ├── eda_preprocessing.ipynb
│   ├── text_chunking_embedding.ipynb
│   └── README.md
├── src/                         # Modular production code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── text_cleaning.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── prompt_templates.py
├── tests/                       # Unit tests
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   └── test_retriever.py
├── app.py                       # Gradio / Streamlit interface
├── requirements.txt
├── README.md
└── .gitignore
```

> 🔍 **Note**: Initial development was notebook-driven for exploration and learning.
> Core logic has been (or is being) **extracted into the `src/` package** to improve maintainability, testability, and production readiness.

---

## ✅ Task 1: Exploratory Data Analysis (EDA) & Preprocessing

### 🎯 Objective

Understand the structure, distribution, and quality of consumer complaint narratives and prepare clean text for downstream NLP tasks.

### 🔍 Key Steps

* Loaded **82,164 complaints** with complete narratives
* Analyzed distribution across financial products
* Analyzed narrative length:

  * Majority are **short (0–250 words)**
  * A small number are **very long (up to ~6,400 words)**
* Visualized narrative length distribution using a histogram
  → Strong right-skewed distribution

### 🧹 Text Cleaning

* Converted text to lowercase
* Removed special characters and boilerplate phrases
* Filtered complaints to include:

  * Credit Cards
  * Personal Loans
  * Savings Accounts
  * Money Transfers

### 📦 Deliverables

* `data/processed/filtered_complaints.csv`
* EDA notebook with visualizations
* Written summary of findings

---

## ✅ Task 2: Text Chunking, Embedding & Vector Store Indexing

### 🎯 Objective

Prepare complaint narratives for **semantic search** by converting them into embeddings and indexing them in a vector database.

### 🔍 Key Steps

### 1️⃣ Sampling

* Stratified sample of **~10,000–15,000 complaints**
* Maintained proportional representation across product categories

### 2️⃣ Chunking

* Split long narratives into overlapping chunks
* Overlap preserved context across chunk boundaries
* Logic later modularized into `src/chunking.py`

### 3️⃣ Embedding

* Used **`sentence-transformers/all-MiniLM-L6-v2`**
* Chosen for speed, small size, and strong semantic performance
* Implemented in `src/embeddings.py`

### 4️⃣ Vector Store Indexing

* Stored embeddings in **FAISS**
* Persisted index to disk
* Stored metadata with each chunk:

  * complaint_id
  * product_category
  * issue / sub-issue
* Metadata handling extracted into reusable functions

### 📦 Deliverables

* Chunking & embedding notebook
* Persisted FAISS index in `vector_store/`
* Modular embedding and indexing logic in `src/`

---

## ✅ Task 3: RAG Core Logic & Evaluation

### 🎯 Objective

Build and evaluate a **retrieval-augmented generation pipeline** using the full-scale pre-built vector store.

### 🧠 RAG Pipeline

1. Embed user query
2. Retrieve top-k relevant complaint chunks
3. Inject retrieved context into a structured prompt
4. Generate grounded answer using an LLM

> ⚠️ **Note on Performance**
> Loading large models (e.g., `Mistral-7B-Instruct`) may take **10–15+ minutes** on CPU-only machines. This is expected behavior.

### 🧩 Prompt Engineering

Prompts instruct the model to:

* Act as a financial analyst
* Use **only provided context**
* Explicitly state when information is insufficient

### 🧪 Evaluation

* 5–10 representative business questions
* Manual qualitative evaluation
* Scored relevance, grounding, and clarity
* Results documented in an evaluation table

### 📦 Deliverables

* Modular RAG logic in `src/rag_pipeline.py`
* Evaluation table and analysis in final report

---

## ✅ Task 4: Interactive Chat Interface

### 🎯 Objective

Provide a **simple, trustworthy UI** for non-technical users.

### 🖥 Features

* Question input box
* Ask / Submit button
* AI-generated answer
* **Source complaint excerpts displayed**
* Clear / Reset functionality
* Optional streaming responses

### 🛠 Tools

* Gradio or Streamlit

### 📦 Deliverables

* `app.py`
* Screenshots / GIFs in final report

---

## 🧪 Testing & Code Quality Improvements

Based on feedback, the project emphasizes:

* ✅ **Extracting notebook logic into `src/` modules**
* ✅ **Explicit metadata handling**
* ✅ **Unit tests for chunking, embeddings, and retrieval**
* ✅ **Cleaner separation between experimentation and production code**

Tests are included under the `tests/` directory to ensure:

* Chunk boundaries are respected
* Embedding dimensions are correct
* Retriever returns relevant results

---

## 🚀 Usage

```bash
pip install -r requirements.txt
python app.py
```

---

## 🧾 Summary

This project demonstrates a full **end-to-end RAG system**:

* **Task 1**: Data understanding and cleaning
* **Task 2**: Chunking, embedding, and vector indexing
* **Task 3**: Retrieval + generation with evaluation
* **Task 4**: Interactive, trust-aware UI

Incorporating reviewer feedback, the project evolves from **notebook-driven exploration** into a **modular, testable, production-oriented system**.

---
