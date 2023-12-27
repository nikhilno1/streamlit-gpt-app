import streamlit as st
from openai import OpenAI
import os
from config import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")
openai_api_key = os.getenv("OPENAI_API_KEY", "")

client = OpenAI(api_key=openai_api_key)

def run_completion(user_input):    
    chat_messages = [{"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}]    
    
    chat_completion = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=chat_messages,
    )    
    result = chat_completion.choices[0].message.content
    return result

