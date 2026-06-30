import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("🚀 AI Startup Foundry")
        st.caption("AI Co-Founder Platform")

        st.divider()

        st.subheader("📌 Navigation")

        st.button("🏠 Home", use_container_width=True)
        st.button("📊 Dashboard", use_container_width=True)
        st.button("📂 Startup History", use_container_width=True)
        st.button("⭐ Saved Ideas", use_container_width=True)
        st.button("⚙ Settings", use_container_width=True)

        st.divider()

        st.subheader("🤖 AI Agents")

        agents = [
            "💡 Idea Validation",
            "📈 Market Research",
            "🏆 Competitor Analysis",
            "💼 Business Model",
            "💰 Financial Planning",
            "🎤 Pitch Deck"
        ]

        for agent in agents:
            st.success(agent)

        st.divider()

        st.subheader("🛠 Technology")

        st.info("Gemini 2.5 Flash")
        st.info("Python")
        st.info("Streamlit")
        st.info("Google ADK (Coming Soon)")
        st.info("MCP Server (Coming Soon)")

        st.divider()

        st.caption("Version 1.0")