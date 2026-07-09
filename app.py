import streamlit as st
import json
import os
import pandas as pd
logo_path = "assets/logo.png"

from groq import Groq
from dotenv import load_dotenv

from services.faq_service import (
    load_faqs,
    build_faq_context,
    add_faq,
    delete_faq,
    update_faq
)
from services.ai_service import get_ai_response
from services.lead_service import (
    save_lead,
    get_business_leads
)
from services.config_service import load_config
from services.email_service import send_lead_notification
from services.analytics_service import (
    save_conversation,
    get_conversations,
    get_most_asked_question
)
config = load_config()

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load FAQ data
faq_data = load_faqs()
faq_context = build_faq_context(faq_data)

st.image(
    logo_path,
    width=180
)

st.title(config["business_name"])

st.markdown(
    """
## 🤖 Your 24/7 AI Receptionist

Never miss another customer enquiry.

Answer questions instantly, capture leads automatically, and provide professional customer support around the clock.

🟢 **Available 24/7**

⚡ **Instant AI Responses**

📞 **Automatic Lead Capture**
"""
)

st.divider()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
st.subheader("💬 Suggested Questions")

for faq in faq_data[:4]:

    if st.button(
        faq["question"],
        use_container_width=True
    ):
        st.session_state["suggested_question"] = faq["question"]
typed_question = st.chat_input(
    "Ask me anything about our business..."
)

user_question = st.session_state.pop(
    "suggested_question",
    None
)

if typed_question:
    user_question = typed_question

if user_question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    answer = get_ai_response(
        user_question,
        faq_context
    )
    st.write("Saving conversation...")
    save_conversation(
        user_question,
        answer
    )
    st.write("Conversation saved.")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
st.divider()

st.subheader("Request a Callback")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")

if st.button("Submit"):

    if not name or not phone:

        st.error(
            "Please enter your name and phone number."
        )

    else:

        business = st.session_state.get("business")

        if business:

            save_lead(
                business["id"],
                name,
                phone
            )

            send_lead_notification(
                name,
                phone
            )

            st.success(
                "Your request has been submitted."
            )

        else:

            st.error(
                "No business is currently logged in."
            )



