import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.business_service import (
    update_business
)

if not is_logged_in():

    st.warning(
        "Please log in."
    )

    st.stop()

business = get_current_business()

st.title("⚙ Business Settings")

business_name = st.text_input(
    "Business Name",
    value=business["business_name"]
)

owner_name = st.text_input(
    "Owner Name",
    value=business["owner_name"]
)

phone = st.text_input(
    "Phone",
    value=business.get("phone", "")
)

welcome_message = st.text_area(
    "Welcome Message",
    value=business.get("welcome_message") or ""
)

ai_personality = st.selectbox(
    "AI Personality",
    [
        "Professional",
        "Friendly",
        "Sales",
        "Technical"
    ],
    index=[
        "Professional",
        "Friendly",
        "Sales",
        "Technical"
    ].index(
        business.get("ai_personality") or "Professional"
    )
)

if st.button("💾 Save Settings"):

    update_business(
        business["id"],
        business_name,
        owner_name,
        phone,
        welcome_message,
        ai_personality
    )

    st.success(
        "Settings Saved!"
    )

    business["business_name"] = business_name
    business["owner_name"] = owner_name
    business["phone"] = phone
    business["welcome_message"] = welcome_message
    business["ai_personality"] = ai_personality

    st.session_state["business"] = business