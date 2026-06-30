import streamlit as st


def metrics():

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🤖 AI Agents", "6")

    c2.metric("⚡ Model", "Gemini")

    c3.metric("💼 Domain", "Business")

    c4.metric("⭐ AI Score", "9.5")