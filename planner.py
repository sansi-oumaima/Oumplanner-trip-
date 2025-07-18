import os
from openai import OpenAI

# ✅ PAS besoin de load_dotenv ici
# Streamlit injecte déjà les variables d’environnement

# 🔒 Clé API prise directement de l’environnement Streamlit Cloud
api_key = os.environ.get("OPENAI_API_KEY")

# 💥 Ajoute une vérification pour éviter plantage silencieux
if not api_key:
    raise ValueError("La clé OPENAI_API_KEY est introuvable. Vérifie les Secrets sur Streamlit Cloud.")

client = OpenAI(api_key=api_key)

def generate_trip(destination: str, days: int, preferences: str) -> str:
    prompt = f"""
    You are a travel expert. Create a travel itinerary for a trip to {destination}
    for {days} days. Preferences: {preferences}. The plan should be day-by-day, concise,
    fun, and suitable for tourists. Use bullet points or numbered days.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
