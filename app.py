# app.py
import gradio as gr
from login import login
from query_model import query_model

def login_interface(username, password):
    login_status, login_message = login(username, password)
    if login_status:
        return gr.update(visible=False), gr.update(visible=True), login_message
    else:
        return gr.update(visible=True), gr.update(visible=False), login_message

def query_interface(platform, api_key, user_question):
    response = query_model(platform, api_key, user_question)
    return response

with gr.Blocks() as demo:
    with gr.Row(visible=True) as login_row:
        username = gr.Textbox(label="Username")
        password = gr.Textbox(label="Password", type="password")
        login_button = gr.Button("Login")
        login_message = gr.Textbox(label="Login Message", interactive=False)
    
    with gr.Row(visible=False) as query_row:
        platform = gr.Radio(choices=["OpenAI", "Anthropic", "Gemini"], label="Select Platform")
        api_key = gr.Textbox(label="API Key", type="password", lines=1)
        user_question = gr.Textbox(label="Enter your question", lines=2, placeholder="Type your question here...")
        query_button = gr.Button("Submit")
        response = gr.Textbox(label="AI Response", interactive=False)
    
    login_button.click(login_interface, inputs=[username, password], outputs=[login_row, query_row, login_message])
    query_button.click(query_interface, inputs=[platform, api_key, user_question], outputs=response)

demo.launch()