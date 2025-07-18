import streamlit as st
import os
import requests

API_URL = "https://huggingface.co/microsoft/DialoGPT-medium"
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_chatbot_response(message):
    payload = {
        "inputs": {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": message
        }
    }
    output = query_huggingface(payload)
    if isinstance(output, dict) and output.get("error"):
        return f"Erreur API : {output['error']}"
    return output[0]["generated_text"]
