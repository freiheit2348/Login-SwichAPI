# query_model.py
from openai import OpenAI
import anthropic
import google.generativeai as genai

def query_model(platform, api_key, user_question):
    if platform == "OpenAI":
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは優秀なAIアドバイザーです。"},
                {"role": "user", "content": user_question}
            ]
        )
        return completion.choices[0].message.content
    elif platform == "Anthropic":
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-2.1",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_question}
            ]
        )
        return message.content[0].text
    elif platform == "Gemini":
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_question)
        return response.text
    else:
        return "Invalid platform selected."