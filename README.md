# ✨ EventEcho

EventEcho turns your event notes into polished, ready to post content for LinkedIn, X, and Instagram. It uses FriendliAI for fast LLM generation and Comet Opik for observability and trace tracking, wrapped in a simple Streamlit interface.

---

## 🚀 Why EventEcho

Every event gives you insights, takeaways, quotes, and raw energy.  
But turning all that into platform-specific social posts takes time.

EventEcho handles the entire flow:

• Paste your event description  
• Paste your notes or transcript  
• Get human sounding posts for LinkedIn, X, and Instagram  
• Click a button to open each platform’s posting flow

The goal is simple:  
Make it effortless to share what you learned.

---

## 🧠 Tech Stack

### **LLM Provider**
- **FriendliAI**  
Used for fast, OpenAI-compatible inference using the `meta-llama-3.1-8b-instruct` model.

### **Observability**
- **Comet / Opik**  
Used for `@track` instrumentation so every generation is logged, traced, and visible inside Opik.

### **Frontend**
- **Streamlit**  
Clean and minimal interface with live generation.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/srodrift/social-ai
cd social-ai