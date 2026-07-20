import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.dashboard_service import (
    get_dashboard_stats,
    get_recent_leads,
    get_recent_conversations
)

from services.analytics_service import (
    get_weekly_conversations
)

from ui.dashboard_cards import dashboard_card
from ui.insights import show_ai_insights
from ui.charts import weekly_conversations_chart

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

stats = get_dashboard_stats(
    business["id"]
)

recent_leads = get_recent_leads(
    business["id"]
)

recent_conversations = get_recent_conversations(
    business["id"]
)

weekly_data = get_weekly_conversations(
    business["id"]
)

# =====================================================

st.title("📊 Dashboard")

st.caption("Theriam AI Receptionist")

st.markdown(f"## {business['business_name']}")

st.success("🟢 Receptionist Online")

st.divider()

# =====================================================
# Dashboard Cards
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    dashboard_card(
        "Leads",
        stats["leads"],
        "👥"
    )

with c2:
    dashboard_card(
        "FAQs",
        stats["faqs"],
        "📚"
    )

with c3:
    dashboard_card(
        "Chats",
        stats["conversations"],
        "💬"
    )

with c4:
    dashboard_card(
        "Health",
        "96%",
        "⭐"
    )

st.divider()

# =====================================================
# Analytics
# =====================================================

weekly_conversations_chart(
    weekly_data
)

st.divider()

# =====================================================
# Main Layout
# =====================================================

left, right = st.columns([2, 1])

with left:

    st.subheader("⚡ Recent Activity")

    if recent_conversations:

        for conversation in recent_conversations:

            with st.container():

                st.markdown(
                    f"**❓ {conversation['question']}**"
                )

                st.caption(
                    conversation["created_at"]
                )

                st.write(
                    conversation["answer"]
                )

                st.divider()

    else:

        st.info(
            "No conversations yet."
        )

with right:

    st.subheader("📞 Recent Leads")

    if recent_leads:

        for lead in recent_leads:

            st.markdown(
                f"**{lead['name']}**"
            )

            st.caption(
                lead["phone"]
            )

            st.divider()

    else:

        st.info(
            "No leads yet."
        )

    st.subheader("🤖 Receptionist")

    st.code(
        f"http://localhost:8501/?slug={business['slug']}"
    )

    show_ai_insights(stats)

st.divider()

st.caption("Theriam AI Receptionist • v0.9.0")