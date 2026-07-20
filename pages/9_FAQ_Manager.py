import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.faq_service import (
    load_faqs,
    add_faq,
    delete_faq,
    update_faq
)

st.set_page_config(
    page_title="FAQ Manager",
    page_icon="📚",
    layout="wide"
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

st.title("📚 FAQ Manager")

st.caption(
    "Manage your AI receptionist knowledge."
)

faqs = load_faqs()

search = st.text_input(
    "🔍 Search FAQs"
)

if search:

    faqs = [
        faq
        for faq in faqs
        if search.lower() in faq["question"].lower()
        or search.lower() in faq["answer"].lower()
    ]

st.divider()

for faq in faqs:

    with st.expander(
        faq["question"],
        expanded=False
    ):

        question = st.text_input(
            "Question",
            faq["question"],
            key=f"q_{faq['id']}"
        )

        answer = st.text_area(
            "Answer",
            faq["answer"],
            key=f"a_{faq['id']}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save",
                key=f"save_{faq['id']}"
            ):

                update_faq(
                    faq["id"],
                    question,
                    answer
                )

                st.success("Saved.")

                st.rerun()

        with col2:

            if st.button(
                "🗑 Delete",
                key=f"delete_{faq['id']}"
            ):

                delete_faq(
                    faq["id"]
                )

                st.success("Deleted.")

                st.rerun()

st.divider()

st.subheader("➕ Add FAQ")

new_question = st.text_input(
    "Question"
)

new_answer = st.text_area(
    "Answer"
)

if st.button(
    "Add FAQ",
    use_container_width=True
):

    if new_question and new_answer:

        add_faq(
            new_question,
            new_answer
        )

        st.success(
            "FAQ Added."
        )

        st.rerun()

    else:

        st.warning(
            "Please complete both fields."
        )