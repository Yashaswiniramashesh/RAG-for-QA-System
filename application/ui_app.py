import streamlit as ui
import requests
import json
import shutil

ui.title("RAG application")
ui.write("")
ui.write("")
ui.write("")

ui.header("Query your RAG!")
ui.write("")
ui.write("")
query = ui.text_input("Enter your question here?", "What is Banana?")
input_obj = {"question": query}
if ui.button('Get answers'):
    res = requests.post(url =  "http://127.0.0.1:8000/ask", data = json.dumps(input_obj) )
    ui.subheader(query)
    ui.subheader("Answer")
    output_obj = json.loads(res.text)
    ui.write(output_obj['llm_response'])
    ui.write("")
    ui.write("")
    ui.write("")

ui.write("")
ui.write("" \
"© 2025 Yashaswini Ramasheshu. All Rights Reserved.")
