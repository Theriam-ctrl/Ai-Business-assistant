import streamlit as st


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )


def get_current_user():

    return st.session_state.get(
        "user"
    )


def get_current_business():

    return st.session_state.get(
        "business"
    )


def logout():

    keys = [
        "logged_in",
        "user",
        "business"
    ]

    for key in keys:

        if key in st.session_state:
            del st.session_state[key]