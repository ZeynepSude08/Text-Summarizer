
import streamlit as st

def ozetle(text):
    return "Bu metnin özeti (örnek)."

def etiketle(text):
    return ["culture", "social issues"]

st.title("Metin Özetleme ve Etiketleme")

text = st.text_area("Metni buraya yapýþtýr")

if st.button("Özetle ve Etiketle"):
    summary = ozetle(text)
    labels = etiketle(text)

    st.write("### Özet:")
    st.write(summary)

    st.write("### Etiketler:")
    st.write(", ".join(labels))
