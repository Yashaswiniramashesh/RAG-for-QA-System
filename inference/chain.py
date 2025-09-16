from ingestion.ingest_and_retrival import IngestRetrieve
from inference.llm import Inference

class Chain:

    def __init__(self):
        self.inference_obj = Inference()
        self.retrieve_obj = IngestRetrieve()

        self.system_prompt = "You are a helpful assistant. Use ONLY the following context and chat history to answer the question. If the answer is not in the context, say 'I don't know'. Chat history includes oldest to latest interactions inorder. You can use the chat history also to answer it.\n\nContext:\n {context}\n\nChat_history:\n {chat_history}\n\nQuestion:\n {query}\n\nAnswer:"

    def format_chat_history(self, chat_history):
        """ Chat_history is the list of dicts, This converts it to string"""
        chat_str = ""
        for ele in reversed(chat_history):
            chat_str += f"\nUSER: {ele['user']}\nASSISTANT: {ele['assistant']}\n\n"
        return chat_str
        
    def get_ans(self, query, chat_history):
        """Makes the LLM Call using context , query and chat history"""
        context_dict = self.retrieve_obj.query_documents(query)
        
        context =  '\n'.join([obj["page_content"] for obj in context_dict])
        chat_str = self.format_chat_history(chat_history=chat_history)
        prompt = self.system_prompt.format(query=query, context=context, chat_history=chat_str)
        response = self.inference_obj.call_llm(prompt = prompt)

        print("++++++++++This is the Prompt++++++++")
        print(prompt)
        print("++++++++++Prompt Ended++++++++")

        answer = {
            "llm_response": response,
            "context_dict" : context_dict
        }
        return answer
    

# if __name__ == '__main__':
#     chain_obj = Chain()
#     chain_obj.get_ans("Bananas have left their mark in which culture?")
