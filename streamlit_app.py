import streamlit as st

# ----------------------------------------
# Components
# ----------------------------------------

from components.styles import load_css
from components.navbar import navbar
from components.hero import hero
from components.metrics import metrics

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI Startup Foundry",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------
# Load CSS
# ----------------------------------------

load_css()

# ----------------------------------------
# Navigation
# ----------------------------------------

navbar()

# ----------------------------------------
# Hero Section
# ----------------------------------------

hero()

# ----------------------------------------
# Platform Overview
# ----------------------------------------

metrics()

st.write("")
st.divider()

# ----------------------------------------
# Startup Idea Section
# ----------------------------------------

st.markdown(
    """
    <h2 style='margin-bottom:5px;'>
        💡 Describe Your Startup Idea
    </h2>

    <p style='color:gray;font-size:17px;'>
        Enter your startup concept and let our AI Co-Founder
        generate a complete business strategy including market
        research, competition analysis, business model,
        financial planning and investor pitch.
    </p>
    """,
    unsafe_allow_html=True
)

startup_idea = st.text_area(
    "Startup Idea",
    placeholder="""
Example:

Build an AI-powered Smart E-Waste Reverse Vending Machine
that rewards users for recycling electronic waste while
helping create a sustainable circular economy.
""",
    height=220,
    label_visibility="collapsed"
)

st.write("")

# ----------------------------------------
# Generate Button
# ----------------------------------------

generate = st.button(
    "🚀 Generate Startup Plan",
    use_container_width=True
)

# ----------------------------------------
# Placeholder Progress
# ----------------------------------------

if generate:

    if startup_idea.strip() == "":

        st.warning("⚠ Please enter a startup idea.")

    else:

        st.success("Startup idea received successfully!")

        st.write("")

        progress = st.progress(0)

        status = st.empty()

        steps = [

            "💡 Validating Startup Idea...",

            "📈 Researching Market...",

            "🏆 Analyzing Competitors...",

            "💼 Designing Business Model...",

            "💰 Preparing Financial Plan...",

            "🎤 Creating Investor Pitch..."

        ]

        for i, step in enumerate(steps):

            status.info(step)

            progress.progress((i + 1) / len(steps))

        status.success("✅ Startup Plan Ready")

        st.write("")

        st.info(
            "🔜 In the next step, these progress stages will call the real AI agents."
        )

        st.divider()

        # ----------------------------------------
        # Placeholder Tabs
        # ----------------------------------------

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "💡 Idea",
            "📈 Market",
            "🏆 Competition",
            "💼 Business",
            "💰 Financial",
            "🎤 Pitch"
        ])

        with tab1:
            st.info("Idea Validation Agent output will appear here.")

        with tab2:
            st.info("Market Research Agent output will appear here.")

        with tab3:
            st.info("Competitor Analysis Agent output will appear here.")

        with tab4:
            st.info("Business Model Agent output will appear here.")

        with tab5:
            st.info("Financial Planning Agent output will appear here.")

        with tab6:
            st.info("Pitch Deck Agent output will appear here.")

# ----------------------------------------
# Footer
# ----------------------------------------

st.divider()

st.markdown(
    """
    <center>

    ### 🚀 AI Startup Foundry

    **AI Co-Founder for Entrepreneurs**

    Powered by **Gemini • Streamlit • Python**

    Google ADK • MCP • Security Layer *(Coming Soon)*

    </center>
    """,
    unsafe_allow_html=True
)