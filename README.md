✨ EventEcho

EventEcho transforms your event notes into polished, platform-ready social posts for LinkedIn, X, and Instagram.  
Built at GitHub Hack Night using FriendliAI for fast LLM inference and Comet Opik for observability.

---

## 🚀 What EventEcho Does

After an event, we all want to post a thoughtful recap. Writing takes time.  
EventEcho does the heavy lifting.

You paste your:
• Event description  
• Notes or transcript  

EventEcho generates:
• A professional LinkedIn post  
• A concise X (Twitter) post under 280 characters  
• An Instagram-style caption with storytelling and hashtags  

All written in a natural, human voice.

---

## 🎯 Features

### Platform-aware post generation
• LinkedIn: reflective, polished  
• X: concise, punchy  
• Instagram: story-first caption with hashtags  

### Powered by FriendliAI  
Uses the Llama-3.1-8B-Instruct model through Friendli’s OpenAI-compatible API.

### Comet Opik Observability  
Every post generation automatically logs:
• Inputs  
• Outputs  
• Latency  
• Metadata  
• Traces for debugging  

### Simple, clean UI  
Streamlit interface with platform buttons to post directly.

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| LLM Provider | FriendliAI |
| Observability | Comet Opik |
| Frontend | Streamlit |
| Language | Python |
| Version Control | GitHub |

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/srodrift/social-ai.git
cd social-ai
