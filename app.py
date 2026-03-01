import streamlit as st
import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("SUPABASE_URL")

def gif_background(path: str, opacity: float = 0.6):
    with open(path, "rb") as f:
        gif = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/gif;base64,{gif}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0, 0, 0,0);
        z-index: 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# Call it with your file
gif_background("test2.gif")

st.set_page_config(page_title="Bonus_Task OneElleven API Visualizer", layout="wide", page_icon="🎬")

# ── STYLES ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { box-sizing: border-box; }

.main {
    background-color: #0f0f1a;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, p, label {
    color: #ffffff !important;
}

/* Inputs */
.stTextInput > div > div > input {
    background-color: #1e1e2e !important;
    border: 1.5px solid #3a3a5c !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #6c63ff !important;
}
.stTextInput > div > div > input::placeholder {
    color: #555577 !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #6c63ff, #ff6b6b);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 32px;
    font-size: 15px;
    font-weight: 600;
    width: 100%;
    margin-top: 8px;
    transition: opacity 0.2s;
}
.stButton > button:hover {
    opacity: 0.88;
    color: white;
}

/* Expander */
.streamlit-expanderHeader {
    background-color: #1e1e2e !important;
    color: #aaaacc !important;
    border-radius: 10px !important;
    font-size: 13px !important;
}

/* Hide branding */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── HEADER ──
st.markdown("""
<div style="
    background: linear-gradient(135deg, #1e1e2e, #6c63ff);
    padding: 20px 32px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 32px;
">
    <div>
        <div style="color: white; font-size: 24px; font-weight: 700;">🎬 Bonus Challenge </div>
        <div style="color: rgba(255,255,255,0.6); font-size: 13px; margin-top: 2px;">API Visualizer</div>
    </div>
    <div style="color: rgba(255,255,255,0.5); font-size: 13px;">v1.0</div>
</div>
""", unsafe_allow_html=True)


# ── INPUT CARD ──
st.markdown("""
<div style="
    background-color: #1e1e2e;
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 28px;
    border: 1px solid #2a2a45;
">
    <div style="color: white; font-size: 17px; font-weight: 600; margin-bottom: 4px;">🔗 Enter your details</div>
    <div style="color: #666688; font-size: 13px; margin-bottom: 20px;">Provide a URL and email to fetch data from the API</div>
""", unsafe_allow_html=True)

url_input   = st.text_input("URL", placeholder="https://example.com/video")
email_input = st.text_input("Email", placeholder="e.g. mfDoom@doomsday.com")
submit      = st.button("🚀 Fetch Data")

st.markdown("</div>", unsafe_allow_html=True)


# ── LOGIC ──
if submit and (url_input or email_input):
    url = f"{base_url}?url={url_input}&email={email_input}"

    with st.spinner("Fetching data..."):
        data = requests.post(url)

    if data.text is not None:

        # Success banner
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #1a3a2a, #20c997);
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        ">
            <span style="font-size: 22px;">✅</span>
            <div>
                <div style="color: white; font-weight: 600;">Data fetched successfully</div>
                <div style="color: rgba(255,255,255,0.65); font-size: 13px;">Response received from the API</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Raw data expander
        st.markdown("---")
        with st.expander("🔍 Developer Tools: View Raw Data"):
            st.code(data.text, language="json")

    else:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #3a1a1a, #fa5252);
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 20px;
        ">
            <div style="color: white; font-weight: 600;">❌ Something went wrong</div>
            <div style="color: rgba(255,255,255,0.65); font-size: 13px; margin-top: 4px;">Please check your URL and email and try again.</div>
        </div>
        """, unsafe_allow_html=True)

elif submit:
    st.markdown("""
    <div style="
        background-color: #2a2a1a;
        border: 1px solid #ffd43b;
        border-radius: 12px;
        padding: 14px 20px;
        color: #ffd43b;
        font-size: 14px;
    ">
        ⚠️ Please enter a URL or email before fetching.
    </div>
    """, unsafe_allow_html=True)


# ── FOOTER ──
st.markdown("""
<div style="
    margin-top: 60px;
    padding: 18px 32px;
    background-color: #1e1e2e;
    border-radius: 12px;
    text-align: center;
    color: rgba(255,255,255,0.3);
    font-size: 13px;
    border: 1px solid #2a2a45;
">
    © 2026 CodingChallenge_PKRampai · API Visualizer
</div>
""", unsafe_allow_html=True)