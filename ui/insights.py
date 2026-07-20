import streamlit as st


def show_ai_insights(stats):

    st.subheader("💡 AI Insights")

    if stats["faqs"] < 10:

        st.warning(
            "You have fewer than 10 FAQs. Add more to improve AI accuracy."
        )

    else:

        st.success(
            "Your FAQ knowledge base looks healthy."
        )

    if stats["leads"] == 0:

        st.info(
            "No leads captured yet. Encourage customers to request callbacks."
        )

    else:

        st.success(
            f"You've captured {stats['leads']} lead(s)."
        )

    if stats["conversations"] == 0:

        st.info(
            "Your receptionist hasn't had any conversations yet."
        )

    else:

        st.success(
            f"Your receptionist has handled {stats['conversations']} conversation(s)."
        )

    if stats["most_asked"] != "No conversations yet":

        st.info(
            f"Most asked question:\n\n{stats['most_asked']}"
        )