import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.faq_service import (
    load_faqs,
    build_faq_context
)

from services.ai_service import (
    get_ai_response
)

if not is_logged_in():

    st.warning(
        "Please log in."
    )

    st.stop()

business = get_current_business()

st.title("🧪 Test My AI")

st.write(
    f"Testing **{business['business_name']}**"
)

faqs = load_faqs(
    business["id"]
)

faq_context = build_faq_context(
    faqs
)

question = st.text_input(
    "Ask your AI anything..."
)

if st.button("Ask AI"):

    if question:

        answer = get_ai_response(
            question,
            business,
            faq_context
        )

        st.success("AI Response")

        st.write(answer)