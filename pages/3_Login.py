import streamlit as st

from services.auth_service import login_user
from services.business_service import get_business_by_user

st.set_page_config(
    page_title="Business Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Welcome Back")

st.caption(
    "Sign in to manage your AI Receptionist."
)

st.divider()

email = st.text_input(
    "Email Address"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button(
    "Login",
    use_container_width=True
):

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

            if not auth.user:

                st.error(
                    "Invalid email or password."
                )

                st.stop()

            business = get_business_by_user(
                auth.user.id
            )

            if not business:

                st.error(
                    "Business profile not found."
                )

                st.stop()

            st.session_state["logged_in"] = True
            st.session_state["user"] = auth.user
            st.session_state["business"] = business

            st.success(
                "✅ Login Successful!"
            )

            st.divider()

            st.subheader(
                f"Welcome back, {business['owner_name']} 👋"
            )

            st.write(
                f"🏢 **{business['business_name']}**"
            )

            st.divider()

            if business.get("onboarding_complete"):

                st.success(
                    "✅ Your business is fully configured."
                )

                st.info(
                    "Open the Dashboard from the sidebar."
                )

            else:

                st.warning(
                    "🚀 Your setup is not complete."
                )

                st.info(
                    "Open the Setup Wizard from the sidebar to finish setting up your AI Receptionist."
                )

        except Exception as e:

            st.error(str(e))