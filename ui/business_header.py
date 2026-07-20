import streamlit as st


def business_header(business):

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title(f"🏢 {business['business_name']}")

        owner = business.get("owner_name") or "Business Owner"

        st.caption(f"Welcome back, {owner}")

    with col2:

        st.success("🟢 Online")

    st.divider()
    st.subheader("📅 Today's Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.info(
            f"""
    **Conversations Today**

    {stats['conversations']}
    """
        )

    with summary_col2:
        st.success(
            f"""
    **Leads Captured**

    {stats['leads']}
    """
        )

    st.divider()