import os
import time
import re
import urllib.parse
import streamlit as st
from openai import OpenAI
from opik import track

# Environment
FRIENDLI_TOKEN = os.getenv("FRIENDLI_TOKEN")
MODEL_ID = os.getenv("FRIENDLI_MODEL_ID", "meta-llama-3.1-8b-instruct")

# API client for Friendli (OpenAI compatible)
client = OpenAI(
    api_key=FRIENDLI_TOKEN,
    base_url="https://api.friendli.ai/serverless/v1",
)

# Streamlit page config
st.set_page_config(
    page_title="EventEcho",
    page_icon="✨",
    layout="wide"
)

# Simple CSS to keep things clean
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Inter', sans-serif; }

    #MainMenu, header, footer {visibility: hidden;}

    .hero {
        background: linear-gradient(135deg, #6B73FF, #000DFF);
        padding: 32px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 24px;
    }

    .hero h1 {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .hero p {
        font-size: 16px;
        opacity: 0.95;
        margin: 0;
    }

    .card {
        background: white;
        padding: 18px 20px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
    }

    .platform-header {
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 8px;
    }

    .platform-sub {
        font-size: 12px;
        color: #4a5568;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
  <h1>✨ EventEcho</h1>
  <p>Turn your event notes into ready to post content for LinkedIn, X, and Instagram.</p>
</div>
""", unsafe_allow_html=True)

# Input section
left, right = st.columns(2)

with left:
    st.markdown('<div class="card"><div style="font-weight:600;font-size:16px;">📍 Event description</div></div>', unsafe_allow_html=True)
    event_description = st.text_area(
        label="",
        height=160,
        placeholder="Example: Hack Night at GitHub with FriendliAI and Comet Opik talks, builders hacking on LLM apps..."
    )

with right:
    st.markdown('<div class="card"><div style="font-weight:600;font-size:16px;">📝 Transcript or notes</div></div>', unsafe_allow_html=True)
    transcript = st.text_area(
        label=" ",
        height=160,
        placeholder="Example: Notes, quotes, rough transcript, bullet points from the event..."
    )

generate = st.button("🚀 Generate social posts", type="primary")


@track
def generate_posts(event_description, transcript):
    prompt = f"""
You are helping someone write social posts about an event they attended.

Inputs:
Event description:
{event_description}

Transcript or notes:
{transcript}

Write three platform specific posts: LinkedIn, Twitter, Instagram.
Make them natural, human, and appropriate for each platform.

Format exactly like this:

LinkedIn:
<post>

Twitter:
<post>

Instagram:
<post>
"""

    messages = [
        {"role": "system", "content": "You write natural, thoughtful social posts that sound human."},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content


if generate:
    if not FRIENDLI_TOKEN:
        st.error("Friendli token is missing in the environment.")
    elif not event_description or not transcript:
        st.error("Please fill in both event description and transcript.")
    else:
        with st.spinner("Generating posts with FriendliAI..."):
            time.sleep(0.5)
            raw_output = generate_posts(event_description, transcript)

        cleaned = raw_output.replace("\r", "").strip()

        patterns = {
            "LinkedIn": r"LinkedIn[:\-]*\s*(.*?)(?=Twitter|Instagram|$)",
            "Twitter": r"Twitter[:\-]*\s*(.*?)(?=Instagram|LinkedIn|$)",
            "Instagram": r"Instagram[:\-]*\s*(.*)$",
        }

        sections = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, cleaned, re.IGNORECASE | re.DOTALL)
            if match:
                sections[key] = match.group(1).strip()
            else:
                sections[key] = "Post not generated."

        st.markdown("---")
        st.subheader("Your generated posts")

        c1, c2, c3 = st.columns(3)

        # LinkedIn
        with c1:
            st.markdown('<div class="platform-header">LinkedIn</div>', unsafe_allow_html=True)
            st.markdown('<div class="platform-sub">Longer and reflective. Good for takeaways and gratitude.</div>', unsafe_allow_html=True)
            linkedin_text = st.text_area("LinkedIn post", sections["LinkedIn"], height=200)
            linkedin_encoded = urllib.parse.quote(linkedin_text)
            linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&summary={linkedin_encoded}"
            st.link_button("Post on LinkedIn", linkedin_url, type="secondary")

        # Twitter / X
        with c2:
            st.markdown('<div class="platform-header">X (Twitter)</div>', unsafe_allow_html=True)
            st.markdown('<div class="platform-sub">Keep it sharp, under 280 characters.</div>', unsafe_allow_html=True)
            twitter_text = st.text_area("X post", sections["Twitter"], height=200)
            twitter_encoded = urllib.parse.quote(twitter_text)
            twitter_url = f"https://twitter.com/intent/tweet?text={twitter_encoded}"
            st.link_button("Post on X", twitter_url, type="secondary")

        # Instagram
        with c3:
            st.markdown('<div class="platform-header">Instagram</div>', unsafe_allow_html=True)
            st.markdown('<div class="platform-sub">Caption for a photo or reel. Copy before posting.</div>', unsafe_allow_html=True)
            instagram_text = st.text_area("Instagram caption", sections["Instagram"], height=200)
            instagram_url = "https://www.instagram.com/accounts/login/"
            st.link_button("Open Instagram", instagram_url, type="secondary")
            st.caption("Instagram does not allow pre filled captions, so copy your text above before you post.")