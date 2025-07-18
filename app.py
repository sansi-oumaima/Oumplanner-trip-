import streamlit as st
from planner import generate_trip

st.set_page_config(page_title="Planificateur de Voyage", page_icon="🌍")
st.title("🌍 Générateur de programme de voyage")

try:
    destination = st.text_input("Destination", placeholder="Ex : Tokyo")
    days = st.slider("Durée du voyage (en jours)", 1, 30, 7)
    preferences = st.text_area("Préférences", placeholder="Ex : gastronomie, musées, nature...")

    if st.button("Générer le programme"):
        with st.spinner("✈️ Génération du programme..."):
            plan = generate_trip(destination, days, preferences)
            st.markdown("## 🗺️ Ton programme de voyage")
            st.markdown(plan)

except Exception as e:
    st.error(f"❌ Une erreur est survenue : {e}")
