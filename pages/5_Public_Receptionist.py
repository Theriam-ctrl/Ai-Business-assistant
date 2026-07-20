import streamlit as st

from services.business_service import get_business_by_slug
from services.faq_service import (
    load_faqs,
    build_faq_context
)
from services.ai_service import get_ai_response
from services.lead_service import save_lead
from services.email_service import send_lead_notification

st.set_page_config(
    page_title="AI Receptionist",
    page_icon="🤖"
)

st.title("🤖 AI Receptionist")

slug = st.text_input(
    "Business Slug",
    placeholder="jiangexplains"
)

if not slug:
    st.stop()

business = get_business_by_slug(slug)

if business is None:
    st.error("Business not found.")
    st.stop()

# ----------------------------------
# Business Branding
# ----------------------------------

if business.get("logo"):
    st.image(
        business["logo"],
        width=180
    )

st.header(
    business["business_name"]
)

welcome = (
    business.get("welcome_message")
    or "Welcome! Ask me anything about our business."
)

st.info(welcome)

st.write(
    """
I'm here to answer your questions instantly.

If I can't answer your question, feel free to request a callback below.
"""
)

st.divider()

# ----------------------------------
# FAQ Context
# ----------------------------------

faqs = load_faqs(
    business["id"]
)

faq_context = build_faq_context(
    faqs
)

# ----------------------------------
# Chat History
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# Chat Input
# ----------------------------------

question = st.chat_input(
    "Ask a question..."
)

if question:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("🤖 AI Receptionist is thinking..."):

            answer = get_ai_response(
                question,
                business,
                faq_context
            )

        st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ----------------------------------
# Callback Form
# ----------------------------------

st.divider()

st.subheader("📞 Request a Callback")

st.write(
    "Leave your details below and we'll contact you."
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
            "Thank you! We'll contact you soon."
        )