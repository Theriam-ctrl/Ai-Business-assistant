import streamlit as st

st.set_page_config(
    page_title="Theriam",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Theriam")

st.subheader(
    "AI Receptionists for South African Businesses"
)

st.markdown(
    """
Welcome to **Theriam**.

Use the sidebar to:

- 📊 Dashboard
- 💬 Conversations
- 👥 Leads
- 💡 AI Insights
- 📚 FAQ Manager
- ⚙️ Settings
- 🌐 Public Receptionist
"""
)

st.info(
    "Select a page from the left sidebar."
)