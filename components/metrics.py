import streamlit as st


def metrics():

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("🤖 AI Agents","6","+100%")

    with c2:
        st.metric("⚡ AI Model","Gemini","2.5 Flash")

    with c3:
        st.metric("💼 Startup Focus","Business","Enterprise")

    with c4:
        st.metric("⭐ Opportunity","9.5 / 10","Excellent")