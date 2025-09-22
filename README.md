# RAG for Question Answering System

This repository contains a fully reproducible code for the RAG pipeline.

---

## Prerequisites

* Python 3.13 (recommended via conda)
* google/gemma-2-2b-it Hugging face token
* (Optional)virtualenv for reproducible environment

## Installation

1. Clone this repository:

   ```bash
   https://github.com/Yashaswiniramashesh/RAG-for-QA-System.git
   cd RAG-for-QA-System
   ```
2. Create and activate environment:

   ```bash
   cd env
   python -m venv env
   source sourceme.sh
   ```
3. Install the requirements
   ```bash
       pip install -r requirements.txt
   ```
5. Set your Hugging Face token:

   ```bash
   export HF_API_TOKEN=""
   ```

6. Add your Data into data/input

## Usage
A. Part 1: Ingestion

   ```bash
   python run_etl.py
   ```
B. Part 2: Querying through the application
   Terminal 1: For the Backend server
   ```bash
   fastapi server_app.py
   ```
   Terminal 2: For the UI server
   ```bash
   streamlit run ui_app.py
   ```
