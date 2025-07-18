import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = "ton_token_ici"  # Remplace par ton token Hugging Face

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
