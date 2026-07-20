import streamlit as st


PRIMARY = "#2563EB"
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"

BACKGROUND = "#0F172A"
CARD = "#1E293B"

TEXT = "#FFFFFF"
SUBTEXT = "#CBD5E1"

BORDER = "#334155"


def apply_theme():

    st.markdown(
        f"""
<style>

.stApp {{
    background-color:{BACKGROUND};
}}

section.main > div {{
    padding-top:2rem;
}}

h1,h2,h3,h4,h5,h6{{
    color:{TEXT};
}}

p,label,span{{
    color:{SUBTEXT};
}}

div[data-testid="stMetric"]{{
    background:{CARD};
    border-radius:14px;
    border:1px solid {BORDER};
    padding:18px;
}}

.stButton>button{{
    border-radius:10px;
    height:45px;
    font-weight:600;
}}

</style>
""",
        unsafe_allow_html=True
    )