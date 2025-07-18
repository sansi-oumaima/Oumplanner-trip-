import streamlit as st

st.title("🌍 Trip Planner avec Hugging Face Chatbot")

user_input = st.text_input("Pose ta question voyage ici :")

if st.button("Envoyer"):
    if user_input.strip():
        with st.spinner("🤖 Génération de la réponse..."):
            response = get_chatbot_response(user_input)
        st.markdown(f"**Chatbot** : {response}")
    else:
        st.warning("Merci d’entrer une question.")
