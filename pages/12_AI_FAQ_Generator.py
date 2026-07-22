import streamlit as st

from services.business_knowledge_service import (
    get_business_knowledge
)

from services.faq_generator_service import (
    generate_faqs
)

from services.faq_service import (
    add_faq,
    delete_all_faqs,
    load_faqs
)

business = st.session_state.get("business")

if not business:

    st.warning(
        "Please log in first."
    )

    st.stop()

st.title("🤖 AI FAQ Generator")

st.caption(
    "Generate professional FAQs for your AI Receptionist."
)

st.divider()

knowledge = get_business_knowledge(
    business["id"]
)

if not knowledge:

    st.warning(
        """
Please import your website first.

Knowledge Centre
→ Website Import
"""
    )

    st.stop()

st.success(
    f"Business: {knowledge['business_name']}"
)

st.write(
    knowledge["description"]
)

st.divider()

if st.button(
    "🚀 Generate FAQs",
    use_container_width=True
):

    with st.spinner(
        "Generating professional FAQs..."
    ):

        st.session_state["generated_faqs"] = (
            generate_faqs(
                knowledge
            )
        )

if "generated_faqs" in st.session_state:

    st.success(
        f"{len(st.session_state['generated_faqs'])} FAQs generated."
    )

    st.info(
        "Review every FAQ before saving."
    )

    for index, faq in enumerate(
        st.session_state["generated_faqs"]
    ):

        with st.expander(
            f"FAQ {index+1}",
            expanded=False
        ):

            question = st.text_input(
                "Question",
                value=faq["question"],
                key=f"question_{index}"
            )

            answer = st.text_area(
                "Answer",
                value=faq["answer"],
                key=f"answer_{index}"
            )

            st.session_state["generated_faqs"][index] = {

                "question": question,

                "answer": answer

            }
            if st.button(
                    "🗑 Remove FAQ",
                    key=f"remove_{index}"
            ):
                st.session_state["generated_faqs"].pop(
                    index
                )

                st.rerun()

    st.divider()

    if st.button(
        "✅ Approve & Save",
        use_container_width=True
    ):

        with st.spinner(
            "Saving FAQs..."
        ):

            delete_all_faqs(
                business["id"]
            )

            for faq in st.session_state[
                "generated_faqs"
            ]:

                add_faq(

                    business["id"],

                    faq["question"],

                    faq["answer"]

                )

            del st.session_state[
                "generated_faqs"
            ]

        st.success(
            "FAQs saved successfully!"
        )

        st.rerun()

st.divider()

st.subheader(
    "Current FAQs"
)

faqs = load_faqs(
    business["id"]
)

if not faqs:

    st.info(
        "No FAQs have been saved yet."
    )

else:

    st.success(
        f"{len(faqs)} FAQs currently live."
    )

    for faq in faqs:

        with st.expander(
            faq["question"]
        ):

            st.write(
                faq["answer"]
            )