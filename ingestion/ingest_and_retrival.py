from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
from langchain_core.documents import Document
import json
from configs.model_api_details import *
from configs.paths import persistant_vdb_path,chunk_output_path

class IngestRetrieve:

    def __init__(self):
        model_kwargs = {'device': 'mps'}
        encode_kwargs = {'normalize_embeddings': False}
        self.hf = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

        #Create a Chroma DB object
        persistant_db_path = persistant_vdb_path
        print(f"Embeddings DB path: {persistant_db_path}")

        #Configuring chroma
        self.vector_store = Chroma(
            collection_name="rag_collection",
            embedding_function=self.hf,
            persist_directory=persistant_db_path  # Where to the vdb save data locally
        )

    def load_documents(self, json_files_path):
        """Ingests the chunked data into vector DB as embeddings"""
        print("**********************Ingesting documents to Vector DB**********************")
        documents = []
        with open(str(json_files_path), "r") as file:
            json_data = json.load(file)
        id_index = []
        print("------Starting ingestion-------")  
        for i, item in enumerate(json_data):
            chunk_content = item.get("content")
            chunk_filename = item.get("file_name")
            id_index.append(str(i))
            each_document = Document(
                id = i,
                page_content=chunk_content,
                metadata={"source": chunk_filename}
            )
            documents.append(each_document)

        uuids = [str(uuid4()) for _ in range(len(documents))]
        self.vector_store.add_documents(documents=documents, ids=uuids)
        
        print(f"Successfully written data from {json_files_path}. Chunks: {len(documents)}")
        print("-------Ingestion Ended---------") 

    def query_documents(self, query):
        #res = self.vector_store.similarity_search(query,k=3)
        #res = self.vector_store.similarity_search_with_score(query, k=3)
        res = self.vector_store.similarity_search_by_vector_with_relevance_scores(embedding=self.hf.embed_query(query), k=10)

        results = []
        for obj in res:
            doc = obj[0].__dict__
            doc['score'] = obj[1]
            results.append(doc)
        
        print(json.dumps(results, indent=4))
        return results

if __name__ == "__main__":
    retrive_obj = IngestRetrieve()
    retrive_obj.load_documents(json_files_path=chunk_output_path)





