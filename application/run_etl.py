from ingestion import extract_v1, chunking,ingest_and_retrival
from configs.paths import *

class Etl:
    
    def __init__(self):
        self.extract_obj = extract_v1.FileParser(extract_input_path,extract_output_path)
        self.chunk_obj = chunking.Chunk(chunk_input_path, chunk_output_path)
        self.vdb_ingest_obj = ingest_and_retrival.IngestRetrieve()
    
    def run_etl_process(self):
        self.extract_obj.parse_files()
        self.chunk_obj.chunk_by_spacy()
        self.vdb_ingest_obj.load_documents(chunked_json_files_path)

if __name__ == "__main__":
    etl_obj = Etl()
    etl_obj.run_etl_process()