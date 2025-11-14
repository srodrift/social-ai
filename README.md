# ✨ Event Social Post Maker

Transform event notes or transcripts into polished social media posts for **LinkedIn**, **Twitter/X**, and **Instagram** in seconds.

This project was built for the GitHub Hack Night using **Friendli AI** for fast LLM inference and **Opik (Comet)** for observability and tracing. The UI is powered by Streamlit with custom design.

---

## 🚀 What This App Does

After attending any event, workshop, conference, or tech meetup, users often want to share a thoughtful recap. But writing posts takes time.

**Event Social Post Maker** solves that.

You paste your:
- Event description  
- Notes or transcript  

And the app instantly generates:
- A professional LinkedIn post  
- A concise Twitter/X post (within 280 chars)  
- A storytelling Instagram caption with hashtags  

All written in a human tone that fits the platform.

---

## 🎯 Features

### 🌐 Platform-specific post generation
- LinkedIn: Long-form insight, professional voice  
- Twitter/X: Tight, high-signal, 280-character limit aware  
- Instagram: Story-driven with relevant hashtags  

### ⚡ Powered by Friendli AI  
Using the serverless Llama 3.1 8B Instruct endpoint

### 📊 Opik LLM Observability
Every generation logs:
- Inputs  
- Outputs  
- Latency  
- Trace metadata  
- Debug information  

Fully integrated with Opik dashboards.

### 🎨 Beautiful custom UI  
- Gradient hero section  
- Clean component cards  
- Copy buttons  
- Responsive 3-column layout  

### 🧩 Future improvements (roadmap)
- File upload: PDF/Doc transcript parser  
- Audio upload → Whisper transcription  
- Hashtag generator  
- Brand voice selector  
- Multi-language posts  
- Eventbrite/Luma link auto-summarizer  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit + custom CSS |
| Backend | Python |
| LLM Provider | Friendli AI (Llama 3.1 8B Instruct) |
| Observability | Opik (Comet) |
| Editor | Cursor |
| Version Control | Git + GitHub |

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/srodrift/social-ai.git
cd social-ai
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

(Open http://localhost:8501)

---

## 🔑 Environment Variables

Set Friendli + Opik:

```bash
export FRIENDLI_TOKEN="your_friendli_token"
export FRIENDLI_MODEL_ID="meta-llama-3.1-8b-instruct"

export OPIK_API_KEY="your_opik_api_key"
export OPIK_WORKSPACE="your_workspace"
export OPIK_PROJECT="Default Project"
```

---

## 🎥 Demo Video

Paste your demo link here:  
https://your-video-link-here.com

---

## 👤 Author

**Sunny Rodrigues**  
Built at GitHub Hack Night in San Francisco.  

---

## ⭐ If you like this project
Give it a ⭐ on GitHub and share it with someone who attends too many events.
