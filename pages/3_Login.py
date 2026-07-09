import streamlit as st

from services.auth_service import login_user
from services.business_service import get_business_by_user

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

                st.session_state["logged_in"] = True
                st.session_state["user"] = auth.user

                business = get_business_by_user(
                    auth.user.id
                )

                st.session_state["business"] = business

                st.success(
                    "Login Successful!"
                )

                business = st.session_state["business"]

                st.success("✅ Login Successful!")

                st.subheader(
                    f"Welcome, {business['owner_name']}!"
                )

                st.write(
                    f"🏢 {business['business_name']}"
                )

            else:

                st.error(
                    "Invalid login."
                )

        except Exception as e:

            st.error(str(e))