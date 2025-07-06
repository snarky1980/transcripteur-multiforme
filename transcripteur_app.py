
import streamlit as st
import openai

client = openai.OpenAI()

st.set_page_config(page_title="Transcripteur Multiforme", layout="centered")
st.title("🎙️ Transcripteur Multiforme")

# API Key à personnaliser ici (à remplacer par ta propre clé API OpenAI)
openai.api_key = "sk-votre-cle-api-ici"

# Entrée utilisateur
texte = st.text_area("📝 Collez ici votre dictée ou transcription brute :", height=200)

# Choix du mode
mode = st.radio("🎯 Choisissez un mode :", ["A - Mot à mot", "B - Propre", "B+ - Propre ajusté", "C - Résumé", "D - Reformulation pro"])

# Choix du sous-style (si D sélectionné)
style = None
if mode.startswith("D"):
    style = st.selectbox("🎨 Sous-style pour la reformulation :", ["D1 - Gouvernemental", "D2 - Courriel professionnel", "D3 - Artistique / lyrique", "D4 - Résumé oral"])

# Bouton d'envoi
if st.button("🚀 Transcrire"):
    if not texte.strip():
        st.warning("Veuillez entrer un texte à transcrire.")
    else:
        prompt = f"Tu es un assistant de transcription. Voici le texte dicté :\n\n{texte}\n\nTranscris-le selon le mode suivant : {mode}"
        if style:
            prompt += f", avec le style {style}."
        prompt += " Ne commente pas, ne donne pas d'explication, seulement le résultat final."

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            st.markdown("---")
            st.subheader("🧾 Résultat :")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Erreur : {str(e)}")
