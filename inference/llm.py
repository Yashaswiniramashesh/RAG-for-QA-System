from huggingface_hub import InferenceClient
from configs.model_api_details import *

class Inference:
	def __init__(self):
		self.client = InferenceClient(api_key=HF_API_TOKEN)

	def call_llm(self, prompt):
		messages = [
			{
				"role": "user",
				"content": prompt
			}
		]

		completion = self.client.chat.completions.create(
		    model= llm_model_name, 
			messages=messages,
			temperature=0.0,
			max_tokens=500
		)
		response = completion.choices[0].message.content
		return response


if __name__ == '__main__':
	"""obj = Inference()
	query = "What are the vitamins in banana?"
	context = "e, and sucrose, making them a quick energy booster. They are rich in dietary fiber, which aids digestion, and contain essential vitamins such as Vitamin C and Vitamin B6, which support immunity and brain health, respectively. Bananas are also high in"
	system_prompt = "You are an intelligent answer generator. Provide the answer given the query and the context at the end. \n\nQuery: {query}\nContext: {context}"
	text = system_prompt.format(query=query, context=context)
	obj.call_llm(prompt=text)
"""