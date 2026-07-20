import streamlit as st

from services.business_loader import require_business
from services.business_service import complete_onboarding

st.set_page_config(
    page_title="Setup Wizard",
    page_icon="🚀",
    layout="wide"
)

business = require_business()

st.title("🚀 Welcome to Theriam")

st.caption(
    "Let's prepare your AI Receptionist."
)

st.progress(0.20)

st.info(
    "This setup takes less than 5 minutes."
)

st.divider()

# ----------------------------------------
# Industry
# ----------------------------------------

industry = st.selectbox(
    "What industry are you in?",
    [
        "Restaurant",
        "Retail",
        "Construction",
        "Plumbing",
        "Electrical",
        "Medical",
        "Legal",
        "Real Estate",
        "Education",
        "Beauty",
        "Automotive",
        "Hospitality",
        "Other"
    ]
)

# ----------------------------------------
# Personality
# ----------------------------------------

personality = st.selectbox(
    "How should your receptionist speak?",
    [
        "Professional",
        "Friendly",
        "Luxury",
        "Casual"
    ]
)

# ----------------------------------------
# Welcome Message
# ----------------------------------------

welcome = st.text_area(
    "Welcome Message",
    value=business.get(
        "welcome_message",
        ""
    ),
    height=120
)

st.divider()

if st.button(
    "Finish Setup",
    use_container_width=True
):

    complete_onboarding(
        business["id"],
        industry,
        welcome,
        personality
    )

    st.success(
        "🎉 Your AI Receptionist is ready!"
    )

    st.balloons()

    st.info(
        "You can now use the Dashboard."
    )