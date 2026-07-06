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
from services.lead_service import save_lead, get_all_leads
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
    save_conversation(
        user_question,
        answer
    )

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

        save_lead(name, phone)

        send_lead_notification(
            name,
            phone
        )

        st.success(
            "Your request has been submitted."
        )

    st.success("Your request has been submitted.")

admin_mode = st.checkbox("Admin Mode")

if admin_mode:

    password = st.text_input(
        "Admin Password",
        type="password"
    )

    if password == config["admin_password"]:

        st.success("Access Granted")

        st.divider()

        st.subheader("Admin Dashboard")
        st.subheader("📚 FAQ Manager")

        new_question = st.text_input(
            "Question"
        )

        new_answer = st.text_area(
            "Answer"
        )

        if st.button("Add FAQ"):

            if new_question and new_answer:
                add_faq(
                    new_question,
                    new_answer
                )

                st.success(
                    "FAQ Added Successfully"
                )

                st.rerun()

        st.subheader("📖 Current FAQs")

        faqs = load_faqs()

        for index, faq in enumerate(faqs):

            st.write(
                f"**Q:** {faq['question']}"
            )

            st.write(
                f"**A:** {faq['answer']}"
            )

            with st.expander(
                    f"✏️ Edit FAQ #{index}"
            ):

                edited_question = st.text_input(
                    "Question",
                    value=faq["question"],
                    key=f"question_{index}"
                )

                edited_answer = st.text_area(
                    "Answer",
                    value=faq["answer"],
                    key=f"answer_{index}"
                )

                if st.button(
                        "💾 Save Changes",
                        key=f"save_{index}"
                ):
                    update_faq(
                        index,
                        edited_question,
                        edited_answer
                    )

                    st.success(
                        "FAQ Updated"
                    )

                    st.rerun()

                if st.button(
                        "🗑 Delete FAQ",
                        key=f"delete_{index}"
                ):
                    delete_faq(index)
                    st.rerun()

            st.divider()

        st.subheader("📊 Analytics")
        conversations = get_conversations()

        st.metric(
            "Total Conversations",
            len(conversations)
        )

        st.metric(
            "Most Asked Question",
            get_most_asked_question()
        )

        leads = get_all_leads()

        st.metric(
            "Total Leads",
            len(leads)
        )
        if leads:
            latest_lead = leads[-1]

            st.subheader("🔥 Latest Lead")

            st.write(
                f"Name: {latest_lead['name']}"
            )

            st.write(
                f"Phone: {latest_lead['phone']}"
            )

            st.write(
                f"Time: {latest_lead['created_at']}"
            )

        leads = get_all_leads()

        if leads:

            df = pd.DataFrame(leads)

            csv = df.to_csv(index=False)

            st.download_button(
                label="📥 Download Leads CSV",
                data=csv,
                file_name="leads.csv",
                mime="text/csv"
            )

            st.table(leads)
            st.subheader("💬 Recent Conversations")

            if conversations:

                for conversation in reversed(conversations[-5:]):
                    with st.expander(
                            conversation["question"]
                    ):
                        st.write(
                            conversation["answer"]
                        )


        else:
            st.info("No leads captured yet.")

    elif password:

        st.error("Incorrect Password")