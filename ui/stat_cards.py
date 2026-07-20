import streamlit as st


def stat_row(cards):

    columns = st.columns(len(cards))

    for column, card in zip(columns, cards):

        with column:

            st.metric(
                card["title"],
                card["value"],
                delta=card.get("delta")
            )