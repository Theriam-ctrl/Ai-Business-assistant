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