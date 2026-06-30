import streamlit as st


def navbar():

    c1, c2, c3, c4, c5 = st.columns([3, 1, 1, 1, 1])

    with c1:
        st.markdown("## 🚀 AI Startup Foundry")

    with c2:
        st.button("Dashboard", use_container_width=True)

    with c3:
        st.button("About", use_container_width=True)

    with c4:
        st.button("GitHub", use_container_width=True)

    with c5:
        st.button("Docs", use_container_width=True)

    st.divider()