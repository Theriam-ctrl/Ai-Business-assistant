import streamlit as st

from services.auth_service import login_user

st.title("🔐 Business Login")

email = st.text_input(
    "Email Address"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if not email or not password:

        st.error(
            "Please enter your email and password."
        )

    else:

        try:

            auth = login_user(
                email,
                password
            )

            if auth.user:

                st.success(
                    "Login Successful!"
                )

            else:

                st.error(
                    "Invalid login."
                )

        except Exception as e:

            st.error(str(e))