import streamlit as st


def page_header(
    title,
    subtitle,
    icon="🤖",
    status="Online"
):

    left, right = st.columns([5, 1])

    with left:

        st.title(
            f"{icon} {title}"
        )

        st.caption(
            subtitle
        )

    with right:

        if status == "Online":

            st.success("🟢 Online")

        elif status == "Offline":

            st.error("🔴 Offline")

        else:

            st.info(status)

    st.divider()