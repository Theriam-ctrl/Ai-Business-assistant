import streamlit as st
from services.lead_service import save_lead
from services.email_service import send_lead_notification
from services.business_service import (
    get_business_by_slug
)

from services.faq_service import (
    load_faqs,
    build_faq_context
)

from services.ai_service import (
    get_ai_response
)

st.title("🤖 AI Receptionist")

slug = st.text_input(
    "Business Slug",
    placeholder="jiangexplains"
)

if slug:

    business = get_business_by_slug(slug)

    if business:

        st.header(
            business["business_name"]
        )

        welcome = (
                business.get("welcome_message")
                or "Welcome! Ask me anything about our business."
        )

        st.info(welcome)

        st.markdown(
            """
        I'm here to answer your questions instantly.

        If I can't help, you can request a callback below and someone from our team will contact you.
        """
        )

        st.divider()

        faq_context = build_faq_context(
            faqs
        )

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input(
            "Ask a question..."
        )

        if question:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):
                st.markdown(question)

            answer = get_ai_response(
                question,
                business,
                faq_context
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.markdown(answer)

    else:

        st.error(
            "Business not found."
        )
        st.divider()

        st.subheader("📞 Request a Callback")

        st.write(
            "Leave your details and a member of our team will contact you."
        )

        customer_name = st.text_input(
            "Your Name"
        )

        customer_phone = st.text_input(
            "Phone Number"
        )

        if st.button("Request Callback"):

            if not customer_name or not customer_phone:

                st.error(
                    "Please complete all fields."
                )

            else:

                save_lead(
                    business["id"],
                    customer_name,
                    customer_phone
                )

                try:

                    send_lead_notification(
                        customer_name,
                        customer_phone
                    )

                except Exception:
                    pass

                st.success(
                    "Thank you! We'll contact you as soon as possible."
                )