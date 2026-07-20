import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)

from services.dashboard_service import (
    get_dashboard_stats
)

st.set_page_config(
    page_title="AI Insights",
    page_icon="💡",
    layout="wide"
)

if not is_logged_in():

    st.warning("Please log in.")
    st.stop()

business = get_current_business()

stats = get_dashboard_stats(
    business["id"]
)

st.title("💡 AI Insights")

st.caption(
    "Recommendations generated from your AI receptionist."
)

st.divider()

# ===========================================
# HEALTH
# ===========================================

health = 100

if stats["faqs"] < 10:
    health -= 20

if stats["leads"] == 0:
    health -= 10

if stats["conversations"] == 0:
    health -= 10

st.subheader("⭐ Business Health")

st.progress(health / 100)

st.metric(
    "Health Score",
    f"{health}%"
)

st.divider()

# ===========================================
# RECOMMENDATIONS
# ===========================================

st.subheader("📋 Recommendations")

if stats["faqs"] < 10:

    st.warning(
        f"You only have {stats['faqs']} FAQs.\n\n"
        "Recommendation: Add more FAQs to improve AI accuracy."
    )

else:

    st.success(
        "Your FAQ knowledge base looks healthy."
    )

if stats["conversations"] == 0:

    st.info(
        "No conversations have been recorded yet."
    )

else:

    st.success(
        f"Your receptionist has handled {stats['conversations']} conversations."
    )

if stats["leads"] == 0:

    st.info(
        "No leads captured yet.\n\n"
        "Recommendation: Encourage visitors to request a callback."
    )

else:

    st.success(
        f"You've captured {stats['leads']} leads."
    )

st.divider()

st.subheader("🔥 Most Asked Question")

st.info(
    stats["most_asked"]
)