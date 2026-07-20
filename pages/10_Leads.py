import streamlit as st
import pandas as pd

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.lead_service import (
    get_business_leads
)

st.set_page_config(
    page_title="Leads",
    page_icon="👥",
    layout="wide"
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

st.title("👥 Leads")

st.caption(
    "Customers who requested a callback."
)

leads = get_business_leads(
    business["id"]
)

if not leads:

    st.info(
        "No leads captured yet."
    )

    st.stop()

search = st.text_input(
    "🔍 Search Leads"
)

rows = []

for lead in leads:

    rows.append(
        {
            "Name": lead["name"],
            "Phone": lead["phone"],
            "Date": lead["created_at"][:19]
        }
    )

df = pd.DataFrame(rows)

if search:

    search = search.lower()

    df = df[
        df["Name"].str.lower().str.contains(search)
        |
        df["Phone"].str.lower().str.contains(search)
    ]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

csv = df.to_csv(index=False)

st.download_button(
    "📥 Export Leads",
    csv,
    "leads.csv",
    "text/csv",
    use_container_width=True
)

st.caption(
    f"{len(df)} lead(s)"
)