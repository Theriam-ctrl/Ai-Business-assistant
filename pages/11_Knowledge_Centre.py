import streamlit as st

from services.website_service import fetch_website
from services.knowledge_service import analyse_business
from services.business_knowledge_service import (
    save_business_knowledge,
    get_business_knowledge
)
from services.faq_generator_service import (
    generate_faqs
)
from services.faq_service import (
    add_faq
)
business = st.session_state.get("business")

if not business:

    st.warning(
        "Please log in first."
    )

    st.stop()

st.title("🧠 Knowledge Centre")

st.caption(
    "Teach your AI Receptionist using your business knowledge."
)

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🌐 Website",
        "🤖 AI FAQs",
        "📚 FAQs",
        "📄 Documents",
        "📝 Notes"
    ]
)

# =====================================================
# WEBSITE
# =====================================================

with tab1:

    st.subheader("Website Import")

    website = st.text_input(
        "Business Website",
        placeholder="https://yourbusiness.co.za"
    )

    if st.button(
        "Import Website",
        use_container_width=True
    ):

        if not website:

            st.error(
                "Please enter a website."
            )

        else:

            with st.spinner(
                "Reading website..."
            ):

                result = fetch_website(
                    website
                )

            if result["success"]:

                st.success(
                    "Website imported successfully."
                )

                with st.spinner(
                    "AI is understanding the business..."
                ):

                    knowledge = analyse_business(
                        result["text"]
                    )

                    save_business_knowledge(
                        business["id"],
                        knowledge
                    )

                st.success(
                    "Business knowledge saved."
                )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Business",
                        knowledge["business_name"]
                    )

                    st.metric(
                        "Industry",
                        knowledge["industry"]
                    )

                with col2:

                    st.metric(
                        "Pages Read",
                        result["pages_read"]
                    )

                    st.metric(
                        "Services Found",
                        len(
                            knowledge["services"]
                        )
                    )

                st.divider()

                st.subheader(
                    "Business Description"
                )

                st.write(
                    knowledge["description"]
                )

                st.subheader(
                    "Target Customers"
                )

                st.write(
                    knowledge["target_customers"]
                )

                st.subheader(
                    "Business Tone"
                )

                st.write(
                    knowledge["tone"]
                )

                st.subheader(
                    "Services"
                )

                for service in knowledge["services"]:

                    st.success(service)

            else:

                st.error(
                    result["error"]
                )

# =====================================================
# AI FAQ GENERATOR
# =====================================================

with tab2:

    st.subheader("🤖 AI FAQ Generator")

    st.write(
        """
Generate professional FAQs automatically from your business knowledge.

The AI will create 20 customer questions and answers which you can
review before publishing them to your AI Receptionist.
"""
    )

    knowledge = get_business_knowledge(
        business["id"]
    )

    if not knowledge:

        st.warning(
            "Please import your website first."
        )

    else:

        if st.button(
            "Generate FAQs",
            use_container_width=True
        ):

            with st.spinner(
                "Generating FAQs..."
            ):

                faqs = generate_faqs(
                    knowledge
                )

                st.session_state["generated_faqs"] = faqs

        if "generated_faqs" in st.session_state:

            st.success(
                f"{len(st.session_state['generated_faqs'])} FAQs generated."
            )

            for index, faq in enumerate(
                st.session_state["generated_faqs"]
            ):

                with st.expander(
                    f"FAQ {index + 1}"
                ):

                    question = st.text_input(
                        "Question",
                        value=faq["question"],
                        key=f"q_{index}"
                    )

                    answer = st.text_area(
                        "Answer",
                        value=faq["answer"],
                        key=f"a_{index}"
                    )

                    st.session_state["generated_faqs"][index] = {
                        "question": question,
                        "answer": answer
                    }

# =====================================================
# DOCUMENTS
# =====================================================

with tab3:

    st.info(
        "Document import coming soon."
    )

# =====================================================
# NOTES
# =====================================================

with tab4:

    st.info(
        "Business notes coming soon."
    )