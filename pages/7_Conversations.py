import streamlit as st
import pandas as pd

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.dashboard_service import (
    get_recent_conversations
)

st.set_page_config(
    page_title="Conversations",
    page_icon="💬",
    layout="wide"
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

st.title("💬 Conversations")

st.caption(
    "Review every conversation handled by your AI receptionist."
)

conversations = get_recent_conversations(
    business["id"],
    limit=100
)

if not conversations:

    st.info(
        "No conversations yet."
    )

    st.stop()

search = st.text_input(
    "🔍 Search conversations"
)

rows = []

for conversation in conversations:

    rows.append(
        {
            "Date": conversation["created_at"][:19],
            "Question": conversation["question"],
            "Answer": conversation["answer"]
        }
    )

df = pd.DataFrame(rows)

if search:

    search = search.lower()

    df = df[
        df["Question"].str.lower().str.contains(search)
        |
        df["Answer"].str.lower().str.contains(search)
    ]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.caption(
    f"{len(df)} conversation(s) found."
)

csv = df.to_csv(index=False)

st.download_button(
    "📥 Export CSV",
    csv,
    "conversations.csv",
    "text/csv",
    use_container_width=True
)