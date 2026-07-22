import streamlit as st

from services.website_service import fetch_website
from services.knowledge_service import analyse_business
from services.business_knowledge_service import save_business_knowledge

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

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🌐 Website",
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
# FAQS
# =====================================================

with tab2:

    st.info(
        "Automatic FAQ generation coming next."
    )

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