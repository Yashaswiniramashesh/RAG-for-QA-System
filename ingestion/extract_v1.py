import os
import csv
import json
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from configs.paths import extract_input_path, extract_output_path


class FileParser:
    def __init__(self, input_path=extract_input_path, output_path=extract_output_path):
        self.input_path = input_path
        self.output_path = output_path
        print("----Extraction Init Complete---")
        

    def extract_text(self, input_file_path):
        ext = os.path.splitext(input_file_path)[-1]
        if ext == '.txt':
            with open(input_file_path, "r") as f:
                return f.read()
        elif ext == '.csv':
            with open(input_file_path, "r") as f:
                rows = []
                reader = csv.reader(f)
                for r in reader:
                    r = " ".join(r)
                    rows.append(r)
                return "\n".join(rows)
        elif ext == '.html':
            with open(input_file_path, "r") as f:
                soup = BeautifulSoup(f, 'html.parser')
                return soup.get_text()
        elif ext == '.pdf':
            text = []
            with open(input_file_path, "rb") as fl:  # Note pdf should be read as binary file
                reader = PdfReader(fl)
                for pg in reader.pages[:2]:
                    text.append(pg.extract_text())
            return " ".join(text)
        else:
            print(f"Unsupported file format: {ext}")
            return ""

    def parse_files(self):
        extracted_text_all = []
        print("------Extraction Starting------")
        print(f"Extracted content read from: {self.input_path}")

        for fname in os.listdir(self.input_path):
            file_path = os.path.join(self.input_path, fname)
            print(f"Extracting{fname}...\n")
            if not os.path.isfile(file_path):
                continue
            temp_extracted_txt = self.extract_text(file_path)
            
            temp_dict = {
            "content" : temp_extracted_txt,
            "file_name" : fname
            }
            extracted_text_all.append(temp_dict)
        with open(self.output_path, "w") as f:
            json.dump(extracted_text_all, f, indent=4)

        print(f"Extracted content written to: {self.output_path}")
        print("------Extraction Complete------")


if __name__ == "__main__":
    
    '''
    import argparse
    parser = argparse.ArgumentParser(description="File parser: extracts content from multiple file types.")
    parser.add_argument("--input_path", required=True, help="Path to the input directory containing files.")
    parser.add_argument("--output_path", required=True, help="Path to the output file (JSON format).")
    args = parser.parse_args()
    print(f"Reading from input path: {args.input_path}")
    parser_instance = FileParser(args.input_path, args.output_path)
    '''
    input_path = "/Users/yashaswiniramasheshu/Documents/DocGPT/data/input"
    output_path = "/Users/yashaswiniramasheshu/Documents/DocGPT/data/output/extracted/extracted.json" 
    print(f"Reading from input path: {input_path}")
    parser_instance = FileParser(input_path, output_path)# passing the path to class objects
    parser_instance.parse_files()
