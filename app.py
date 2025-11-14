import os
import time
import re
import importlib
import streamlit as st
from openai import OpenAI
from opik import track

# Environment
FRIENDLI_TOKEN = os.getenv("FRIENDLI_TOKEN")
MODEL_ID = os.getenv("FRIENDLI_MODEL_ID", "meta-llama-3.1-8b-instruct")

# API client
client = OpenAI(
    api_key=FRIENDLI_TOKEN,
    base_url="https://api.friendli.ai/serverless/v1",
)

# Streamlit page config
st.set_page_config(
    page_title="Event Social Post Maker",
    page_icon="✨",
    layout="wide"
)

# ============== CSS UI ==============
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu, header, footer {visibility: hidden;}

    .hero {
        background: linear-gradient(135deg, #6B73FF, #000DFF);
        padding: 40px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.95;
    }

    .input-card {
        background: white;
        padding: 20px 25px;
        border-radius: 14px;
        border: 1px solid #eaeaea;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .platform-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #eaeaea;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    .copy-btn {
        background: #4CAF50;
        color: white;
        padding: 10px 18px;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s;
    }

    .copy-btn:hover {
        opacity: 0.85;
    }

</style>
""", unsafe_allow_html=True)

# ============== HERO SECTION ==============
st.markdown("""
<div class="hero">
    <h1>✨ Event Social Post Maker</h1>
    <p>Transform your event experiences into engaging social media posts</p>
</div>
""", unsafe_allow_html=True)


# ============== INPUT SECTION ==============
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-card"><h3>📍 Event Description</h3></div>', unsafe_allow_html=True)
    event_description = st.text_area("", height=170, placeholder="Describe the event...")

with col2:
    st.markdown('<div class="input-card"><h3>📝 Transcript or Notes</h3></div>', unsafe_allow_html=True)
    transcript = st.text_area("", height=170, placeholder="Paste raw notes or transcript...")


# ============== GENERATE BUTTON ==============
generate = st.button("🚀 Generate Social Posts")

# ============== LLM FUNCTION ==============
@track
def generate_posts(event_description, transcript):
    prompt = f"""
You are helping someone write social posts about an event they attended.

Inputs:
Event description:
{event_description}

Transcript or notes:
{transcript}

Write three platform-specific posts: LinkedIn, Twitter, Instagram.
Follow each platform's tone and rules. Make them human, thoughtful and natural.
Format exactly like:

LinkedIn:
<post>

Twitter:
<post>

Instagram:
<post>
"""

    messages = [
        {"role": "system", "content": "You write natural human social posts."},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


# ============== GENERATION LOGIC ==============
if generate:
    if not FRIENDLI_TOKEN:
        st.error("Friendli token missing.")
    elif not event_description or not transcript:
        st.error("Please enter both event description and transcript.")
    else:
        with st.spinner("Generating posts..."):
            time.sleep(1)
            raw_output = generate_posts(event_description, transcript)

        # Clean output
        clean = raw_output.replace("\r", "").strip()

        # Bulletproof regex extraction
        patterns = {
            "LinkedIn": r"LinkedIn[:\-]*\s*(.*?)(?=Twitter|Instagram|$)",
            "Twitter": r"Twitter[:\-]*\s*(.*?)(?=Instagram|LinkedIn|$)",
            "Instagram": r"Instagram[:\-]*\s*(.*)$",
        }

        sections = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, clean, re.IGNORECASE | re.DOTALL)
            if match:
                sections[key] = match.group(1).strip()
            else:
                sections[key] = "Post not generated."

        st.markdown("---")
        st.header("Your Generated Posts")

        # Output columns
        c1, c2, c3 = st.columns(3)

        with c1:
            st.subheader("LinkedIn")
            linkedin_text = st.text_area(" ", sections["LinkedIn"], height=200)
            if st.button("Copy LinkedIn"):
                st.success("Copied!")

        with c2:
            st.subheader("Twitter / X")
            twitter_text = st.text_area("  ", sections["Twitter"], height=200)
            if st.button("Copy Twitter"):
                st.success("Copied!")

        with c3:
            st.subheader("Instagram")
            instagram_text = st.text_area("   ", sections["Instagram"], height=200)
            if st.button("Copy Instagram"):
                st.success("Copied!")