import os
from openai import OpenAI

# Obtenir la clé directement depuis l’environnement Streamlit Cloud
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_trip(destination: str, days: int, preferences: str) -> str:
    prompt = f"""
    You are a travel expert. Create a travel itinerary for a trip to {destination}
    for {days} days. Preferences: {preferences}. The plan should be day-by-day, concise,
    fun, and suitable for tourists. Use bullet points or numbered days.
    """

    response = client.chat.completions.create(
        model="gpt-4",  # ou "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
