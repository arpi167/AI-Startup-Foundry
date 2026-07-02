import streamlit as st


def navbar():

    col1, col2, col3 = st.columns([5, 2, 2])

    with col1:
        st.markdown("""
        <h2 style="margin-top:5px;">
        🚀 AI Startup Foundry
        </h2>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align:right;padding-top:12px;">
            <b>Dashboard</b> &nbsp;&nbsp;
            About &nbsp;&nbsp;
            Docs
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align:right;padding-top:8px;">
            <button style="
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px 18px;
                font-weight:bold;
                cursor:pointer;
            ">
            GitHub
            </button>
        </div>
        """, unsafe_allow_html=True)

    st.divider()