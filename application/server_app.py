from fastapi import FastAPI
from pydantic import BaseModel
from inference.chain import Chain

app = FastAPI()
obj = Chain()
chat_history = []


class InputReq(BaseModel):
    question : str

@app.get("/")
def list_methods():
    methods =  {
        "ask_question" : "/ask",
        "upload_file" : "/upload"
    }
    return methods

@app.post("/ask")
def ask_question(request: InputReq):
    question = request.question
    chain_response = obj.get_ans(question, chat_history)
    hist_obj = {"user" : question , "assistant" : chain_response["llm_response"]}
    chat_history.append(hist_obj)
    print("---------------------------LLM Response and Context ------------------------")
    print(chain_response["llm_response"])
    return chain_response