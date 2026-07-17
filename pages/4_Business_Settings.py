import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.business_service import (
    update_business,
    update_business_logo
)

from services.storage_service import (
    upload_logo
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

st.title("⚙ Business Settings")

# -----------------------------
# Logo
# -----------------------------

if business.get("logo"):

    st.image(
        business["logo"],
        width=200
    )

else:

    st.info("No logo uploaded yet.")

logo_file = st.file_uploader(
    "Upload Business Logo",
    type=["png", "jpg", "jpeg"]
)

if st.button("📤 Upload Logo"):

    if logo_file is None:

        st.error("Please choose a logo first.")

    else:

        logo_url = upload_logo(
            logo_file,
            business["slug"]
        )

        update_business_logo(
            business["id"],
            logo_url
        )

        # Update the session copy
        business["logo"] = logo_url
        st.session_state["business"] = business

        st.success("Logo uploaded successfully!")

        st.rerun()

st.divider()

# -----------------------------
# Business Details
# -----------------------------

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

    business["business_name"] = business_name
    business["owner_name"] = owner_name
    business["phone"] = phone
    business["welcome_message"] = welcome_message
    business["ai_personality"] = ai_personality

    st.session_state["business"] = business

    st.success("Settings Saved!")

