from services.business_service import create_business
import streamlit as st

st.title("🏢 Register Your Business")

business_name = st.text_input(
    "Business Name"
)

owner_name = st.text_input(
    "Owner Name"
)

email = st.text_input(
    "Email Address"
)

password = st.text_input(
    "Password",
    type="password"
)

confirm_password = st.text_input(
    "Confirm Password",
    type="password"
)

if st.button("Create Account"):

    if not all([
        business_name,
        owner_name,
        email,
        password,
        confirm_password
    ]):

        st.error(
            "Please complete every field."
        )

    elif password != confirm_password:

        st.error(
            "Passwords do not match."
        )

    else:

        create_business(
            business_name,
            owner_name,
            email,
            password
        )

        st.success(
            "Business registered successfully!"
        )