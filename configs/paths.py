
#For extracting : used in extract_v1.py, used for the fileparser obj
extract_input_path = "data/input"
extract_output_path = "data/output/extracted/extracted.json" 


#For chunking : used in chunking.py, used for the chunk obj
chunk_input_path = extract_output_path
chunk_output_path = "data/output/extracted/chunked.json"

#Vector db path for persistance
persistant_vdb_path = "data/rag_chroma_db"

#Loading chunks to vector db path, used in IngestRetrieve.load_documents
chunked_json_files_path = chunk_output_path