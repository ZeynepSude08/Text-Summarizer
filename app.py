
import streamlit as st

def ozetle(text):
    return "Bu metnin �zeti (�rnek)."

def etiketle(text):
    return ["culture", "social issues"]

st.title("Metin �zetleme ve Etiketleme")

text = st.text_area("Metni buraya yap��t�r")

if st.button("�zetle ve Etiketle"):
    summary = ozetle(text)
    labels = etiketle(text)

    st.write("### �zet:")
    st.write(summary)

    st.write("### Etiketler:")
    st.write(", ".join(labels))
