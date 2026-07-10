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

from services.lead_service import (
    get_business_leads
)

from services.config_service import load_config

from services.session_service import (
    is_logged_in,
    get_current_business
)

config = load_config()

if not is_logged_in():

    st.warning(
        "Please log in to access the Admin Dashboard."
    )

    st.stop()

business = get_current_business()

st.title("🛠 Admin Dashboard")

st.success(
    f"Welcome, {business['owner_name']}!"
)

st.caption(
    f"🏢 {business['business_name']}"
)

st.divider()

# ==========================
# FAQ MANAGER
# ==========================

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

    st.write(f"**Q:** {faq['question']}")
    st.write(f"**A:** {faq['answer']}")

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

# ==========================
# ANALYTICS
# ==========================

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

leads = get_business_leads(
    business["id"]
)

st.metric(
    "Total Leads",
    len(leads)
)

# ==========================
# LATEST LEAD
# ==========================

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

else:

    st.info(
        "No leads captured yet."
    )

# ==========================
# LEADS TABLE
# ==========================

st.subheader("📋 All Leads")

lead_df = pd.DataFrame(leads)

st.dataframe(
    lead_df,
    use_container_width=True
)

csv = lead_df.to_csv(
    index=False
)

st.download_button(
    "⬇ Download Leads CSV",
    csv,
    "leads.csv",
    "text/csv"
)
