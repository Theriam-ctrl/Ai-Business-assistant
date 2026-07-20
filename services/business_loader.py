import streamlit as st

from services.session_service import (
    is_logged_in,
    get_current_business
)


def require_business():
    """
    Ensures a business is logged in.

    Returns the current business.

    Stops execution if no business exists.
    """

    if not is_logged_in():

        st.warning(
            "Please log in."
        )

        st.stop()

    business = get_current_business()

    if not business:

        st.error(
            "Business session not found."
        )

        st.stop()

    return business