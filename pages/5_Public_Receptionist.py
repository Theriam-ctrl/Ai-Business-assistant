import streamlit as st

from services.business_service import (
    get_business_by_slug
)

st.title("🤖 Public AI Receptionist")

slug = st.text_input(
    "Business Slug",
    placeholder="jiang-explains"
)

if slug:

    business = get_business_by_slug(slug)

    if business:

        st.success(
            f"Loaded {business['business_name']}"
        )

        st.write(business)

    else:

        st.error(
            "Business not found."
        )