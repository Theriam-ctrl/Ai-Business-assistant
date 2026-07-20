import streamlit as st


def dashboard_card(title, value, icon):

    st.markdown(
        f"""
        <style>

        .theriam-card {{
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border: 1px solid #334155;
            border-left: 5px solid #3b82f6;
            border-radius: 18px;
            padding: 22px;
            min-height: 170px;
            transition: all 0.3s ease;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
            margin-bottom: 15px;
        }}

        .theriam-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0px 18px 35px rgba(0,0,0,0.35);
            border-left: 5px solid #22c55e;
        }}

        .theriam-icon {{
            font-size: 40px;
            margin-bottom: 15px;
        }}

        .theriam-title {{
            font-size: 17px;
            color: #94a3b8;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}

        .theriam-value {{
            font-size: 42px;
            color: white;
            font-weight: 700;
            margin-top: 12px;
            word-wrap: break-word;
        }}

        </style>

        <div class="theriam-card">

            <div class="theriam-icon">
                {icon}
            </div>

            <div class="theriam-title">
                {title}
            </div>

            <div class="theriam-value">
                {value}
            </div>

        </div>

        """,
        unsafe_allow_html=True
    )