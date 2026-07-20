import streamlit as st


def page_header(title, subtitle=None, status=None):

    left, right = st.columns([4, 1])

    with left:

        st.title(title)

        if subtitle:
            st.caption(subtitle)

    with right:

        if status:

            if status.lower() == "online":

                st.success("🟢 Online")

            elif status.lower() == "offline":

                st.error("🔴 Offline")

            else:

                st.info(status)

    st.divider()