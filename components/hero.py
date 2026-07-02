import streamlit as st


def hero():

    left, right = st.columns([2,1])

    with left:

        st.markdown("""
        <div style="padding-top:20px;">

        <h1 style="
        font-size:48px;
        margin-bottom:10px;
        ">
        🚀 AI Startup Foundry
        </h1>

        <h3 style="
        color:#2563EB;
        margin-top:0px;
        ">
        AI Co-Founder for Entrepreneurs
        </h3>

        <p style="
        font-size:18px;
        color:gray;
        line-height:1.8;
        ">
        Turn startup ideas into investor-ready businesses
        using multiple AI agents powered by Gemini.
        Generate market research, financial plans,
        business models and investor pitches instantly.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""

        <div style="
        background:linear-gradient(135deg,#2563EB,#1D4ED8);
        height:260px;
        border-radius:20px;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;
        text-align:center;
        ">

        <div>

        <h1>🤖</h1>

        <h3>6 AI Agents</h3>

        <p>Working Together</p>

        </div>

        </div>

        """, unsafe_allow_html=True)

    st.write("")