import json
import spacy
from configs.paths import chunk_input_path, chunk_output_path
from configs.model_api_details import chunk_size
class Chunk:
    def __init__(self, input_path=chunk_input_path, output_path=chunk_output_path):
        self.input_path = input_path
        self.output_path = output_path
        print("----Chunking Init Complete-----")
        with open(self.input_path, "r") as file:
            self.json_data = json.load(file)

    def chunk_by_words(self, step=chunk_size):
        extracted_text_all = []
        for each_doc in self.json_data:
            text = each_doc["content"]
            file_name = each_doc["file_name"]
            chunk_list = [text[i:i + step] for i in range(0, len(text), step)]
            print(f"{file_name} chunks count = {len(chunk_list)}")
            for each_chunk in chunk_list:
                temp_dict = {
                    "content": each_chunk,
                    "file_name": file_name
                }
                extracted_text_all.append(temp_dict)
        self.save_to_json(extracted_text_all)

    def chunk_by_spacy(self):
        ("--------Chunking Started-------")
        print("Chunking data input path:"+self.input_path)
        extracted_text_all = []
        nlp = spacy.load('en_core_web_sm')
        for each_doc in self.json_data:
            fname = each_doc["file_name"]
            text = each_doc["content"]
            doc = nlp(text)
            chunk_num = 0
            for sent in doc.sents:
                extracted_text_all.append({"content": str(sent), "file_name": fname})
                chunk_num += 1
            print(f"{fname} loaded {chunk_num} chunks...")

        #add number of sents as params
        self.save_to_json(extracted_text_all)      

    def save_to_json(self, chunked_words):
        with open(self.output_path, "w") as f:
            json.dump(chunked_words, f, indent=4)
        print("Chunks written as JSON , Chunked Path:"+ self.output_path)
        print("-------Chunking Complete-------")

if __name__ == "__main__":
    input_path = "/Users/yashaswiniramasheshu/Documents/DocGPT/data/output/extracted/extracted.json"
    output_path = "/Users/yashaswiniramasheshu/Documents/DocGPT/data/output/extracted/chunked.json"
    print(f"Reading from input path: {input_path}")
    chunk_obj = Chunk(input_path, output_path)
    chunk_obj.chunk_by_spacy()
    #chunk_obj.chunk_by_words()