import pandas as pd
import streamlit as st


def weekly_conversations_chart(data):
    """
    Displays a weekly conversations chart.

    data should look like:

    {
        "Mon": 4,
        "Tue": 8,
        ...
    }
    """

    st.subheader("📈 Conversations This Week")

    df = pd.DataFrame(
        {
            "Day": list(data.keys()),
            "Conversations": list(data.values())
        }
    )

    st.bar_chart(
        df,
        x="Day",
        y="Conversations",
        use_container_width=True
    )