import streamlit as st
import numpy as np

st.set_page_config(page_title="FX Builder para Vocais", layout="wide")

st.title("🎛️ FX Builder para Vocais")
st.markdown("Simulador visual de efeitos vocais — delay, reverb, vocoder e glitch FX.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔊 Delay")
    delay_on = st.toggle("Ativar Delay", value=True)
    delay_time = st.slider("Tempo (ms)", 50, 2000, 400)
    delay_feedback = st.slider("Feedback (%)", 0, 95, 30)
    delay_mix = st.slider("Mix (%)", 0, 100, 60)

with col2:
    st.subheader("🌫️ Reverb")
    reverb_on = st.toggle("Ativar Reverb", value=True)
    reverb_size = st.slider("Tamanho da Sala", 0.0, 1.0, 0.6)
    reverb_damp = st.slider("Damping", 0.0, 1.0, 0.3)
    reverb_mix = st.slider("Mix (%)", 0, 100, 50)

with col3:
    st.subheader("🤖 Vocoder / Glitch FX")
    vocoder_on = st.toggle("Ativar Vocoder", value=False)
    glitch_amount = st.slider("Glitch Intensity", 0, 100, 20)
    pitch_shift = st.slider("Pitch Shift (semitons)", -12, 12, 0)

st.divider()
st.subheader("🎧 Visualização Geral")

st.markdown(f"""
- **Delay**: {'Ligado' if delay_on else 'Desligado'} | Tempo: {delay_time} ms | Feedback: {delay_feedback}% | Mix: {delay_mix}%
- **Reverb**: {'Ligado' if reverb_on else 'Desligado'} | Tamanho: {reverb_size} | Damping: {reverb_damp} | Mix: {reverb_mix}%
- **Vocoder/Glitch**: {'Ligado' if vocoder_on else 'Desligado'} | Glitch: {glitch_amount}% | Pitch Shift: {pitch_shift} semitons
""")
