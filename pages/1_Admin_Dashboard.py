import streamlit as st
import pandas as pd

from services.faq_service import (
    load_faqs,
    add_faq,
    update_faq,
    delete_faq
)

from services.analytics_service import (
    get_conversations,
    get_most_asked_question
)

from services.lead_service import get_all_leads
from services.config_service import load_config

config = load_config()

st.title("🛠 Admin Dashboard")

password = st.text_input(
    "Admin Password",
    type="password"
)

if password == config["admin_password"]:

    st.success("Access Granted")

    st.divider()

    # FAQ Manager

    st.subheader("📚 FAQ Manager")

    new_question = st.text_input("Question")
    new_answer = st.text_area("Answer")

    if st.button("Add FAQ"):

        if new_question and new_answer:

            add_faq(
                new_question,
                new_answer
            )

            st.success("FAQ Added Successfully")

            st.rerun()

    st.subheader("📖 Current FAQs")

    faqs = load_faqs()

    for index, faq in enumerate(faqs):

        st.write(f"**Q:** {faq['question']}")
        st.write(f"**A:** {faq['answer']}")

        with st.expander(f"✏️ Edit FAQ #{index}"):

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

                st.success("FAQ Updated")

                st.rerun()

            if st.button(
                "🗑 Delete FAQ",
                key=f"delete_{index}"
            ):

                delete_faq(index)

                st.rerun()

        st.divider()

    # Analytics

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

    # Latest Lead

    if leads:

        latest_lead = leads[-1]

        st.subheader("🔥 Latest Lead")

        st.write(f"Name: {latest_lead['name']}")
        st.write(f"Phone: {latest_lead['phone']}")
        st.write(f"Time: {latest_lead['created_at']}")
        # Download Leads

        df = pd.DataFrame(leads)

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download Leads CSV",
            data=csv,
            file_name="leads.csv",
            mime="text/csv"
        )

        st.table(leads)
        # Recent Conversations

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

            st.info("No conversations yet.")

elif password:

    st.error("Incorrect Password")