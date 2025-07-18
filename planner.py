import streamlit as st
import os
from openai import OpenAI

# 🔐 Récupération de la clé depuis les secrets
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La clé OPENAI_API_KEY est introuvable. Vérifie les secrets Streamlit Cloud.")

# Initialisation client OpenAI
client = OpenAI(api_key=api_key)

# Fonction de génération
def generate_trip(destination: str, days: int, preferences: str) -> str:
    prompt = f"""
    You are a travel expert. Create a travel itinerary for a trip to {destination}
    for {days} days. Preferences: {preferences}. The plan should be day-by-day, concise,
    fun, and suitable for tourists. Use bullet points or numbered days.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# 🎨 Interface utilisateur Streamlit
st.set_page_config(page_title="Trip Planner AI", page_icon="🌍")
st.title("🌍 Trip Planner with GPT-4")
st.write("Planifie ton voyage en quelques secondes grâce à l'IA !")

# Champs utilisateur
destination = st.text_input("🏖️ Destination", placeholder="Ex : Brésil, Japon, Bali...")
days = st.number_input("📅 Nombre de jours", min_value=1, max_value=30, value=7)
preferences = st.text_area("🎯 Tes préférences", placeholder="Nature, plages, nourriture halal, activités aventure...")

# Bouton de génération
if st.button("✈️ Générer mon programme"):
    with st.spinner("✈️ Génération de ton plan de voyage..."):
        trip_plan = generate_trip(destination, days, preferences)
        st.success("🎉 Voici ton programme de voyage :")
        st.markdown(trip_plan)
