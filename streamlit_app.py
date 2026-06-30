import streamlit as st

from components.styles import load_css

from components.hero import hero

from components.navbar import navbar

st.set_page_config(
    page_title="AI Startup Foundry",
    page_icon="🚀",
    layout="wide"
)

load_css()
navbar()

hero()
from components.metrics import metrics

metrics()

st.write("")

st.subheader("💡 Startup Idea")

startup_idea = st.text_area(
    "Startup Idea",
    height=180,
    placeholder="Describe your startup idea...",
    label_visibility="collapsed"
)

if st.button("🚀 Generate Startup Plan"):

    if startup_idea.strip():

        st.success("Ready! Agent execution will be connected next.")

    else:

        st.warning("Please enter a startup idea.")