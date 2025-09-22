import os


load_dotenv("../env/.env")
#LLM details
llm_model_name = "google/gemma-2-2b-it"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

#Embedding Model details
embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
chunk_size = 250 