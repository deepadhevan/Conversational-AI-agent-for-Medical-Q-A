# Conversational-AI-agent-for-Medical-Q-A
A conversational agent for real-time, evidence-based medical Q&amp;A.
# MedSearch

A conversational agent for real-time, evidence-based medical question answering powered by GPT-4 Turbo.

---

## Overview

MedSearch is a modular, extendable medical Q&A system designed to provide real-time, evidence-based answers to medical queries using a retrieval-augmented generation (RAG) approach combined with large language models. This version integrates a GPT-4 Turbo-like ensemble (mocked) with a biomedical passage retriever and simple NLU modules.

This project showcases a deployable pipeline featuring:

- **Natural Language Understanding (NLU)**
- **Evidence Retrieval from medical corpus**
- **Ensemble of GPT-4 Turbo models for answer generation**
- **Answer aggregation for consensus**
- **FastAPI web interface with example UI**

---

## Features

- Modular Python package for easy swapping of components
- Evidence-grounded medical answers referencing retrieved documents
- Simple web API and interactive question-answer UI
- Container-ready (Dockerfile included)
- Designed for extensibility and reproducibility

---

## Getting Started

### Prerequisites

- Python 3.8+
- SQLite database with pre-indexed medical passages and embeddings (`data/med_corpus.db`). Example dataset or indexing code should be prepared separately.
- Optional: GPU for transformer models in retrieval



