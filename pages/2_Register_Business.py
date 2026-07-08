from services.business_service import create_business
import streamlit as st
from services.auth_service import register_user

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

        try:

            auth = register_user(
                email,
                password
            )

            if auth.user:

                create_business(
                    auth.user.id,
                    business_name,
                    owner_name,
                    email
                )

                st.success(
                    "Business registered successfully!"
                )

            else:

                st.error(
                    "Registration failed."
                )

        except Exception as e:

            st.error(str(e))