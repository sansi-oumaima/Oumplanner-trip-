import os
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_chatbot_response(message):
    if not message:
        return "Merci d'entrer une question."
    payload = {"inputs": message}
    output = query_huggingface(payload)
    if isinstance(output, dict) and output.get("error"):
        return f"Erreur API : {output['error']}"
    return output[0]["generated_text"] if isinstance(output, list) else str(output)
