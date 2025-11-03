# Persona-Adaptive Customer Support Agent

An intelligent **AI-powered support assistant** that dynamically adapts its responses based on the **customer’s persona** — such as *Frustrated User*, *Technical Expert*, or *Business Executive*.  

It leverages **LangChain**, **Gemini LLM**, and a **Chroma Vector Database** to deliver **context-aware**, **emotionally adaptive**, and **persona-aligned** responses for smarter customer interactions.

---

##  Project Overview

###  Goal
To build a Customer Support Chatbot that can:
-  Detect the user’s persona — analyze tone, sentiment, and technical depth of queries.  
-  Retrieve relevant **knowledge base (KB)** content using semantic search.  
-  Adapt its response tone and style based on persona (*empathetic*, *formal*, or *technical*).  
-  Escalate unresolved or critical issues to human agents with full conversation context.  

---

##  Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | Flask, LangChain |
| **LLM Model** | Gemini |
| **Vector Store** | ChromaDB |
| **Programming Language** | Python |
| **Environment Management** | dotenv |
| **Persona Logic** | JSON / Rule-based Detection |

---

##  Key Features

-  **Persona Detection:** Analyzes tone, sentiment, and intent to classify users (e.g., *Frustrated*, *Business*, *Technical*).  
-  **Knowledge Retrieval:** Employs **ChromaDB** for semantic document retrieval from the KB.  
-  **Adaptive Response:** Adjusts tone, formality, and complexity according to persona type.  
-  **Contextual Escalation:** Hands off complex issues to human agents with summarized context.  
-  **Emotion Awareness:** Integrates empathy and human-like tone for better user satisfaction.  

---

##  Architecture

```text
User Query
   ↓
Persona Detection (Sentiment + Intent)
   ↓
Knowledge Retrieval (Chroma Vector Search)
   ↓
Adaptive Response Generation (LLM)
   ↓
Contextual Reply

##  Setup Instructions &  Example Workflow

# 1. Install Dependencies
pip install -r requirements.txt

# 2. Generate Vector Store
python -c "from rag_retriever import create_vector_db; create_vector_db()"

# 3. Run the Application
python app.py

# 🧠 Running the Chatbot
# Start the Flask API
python main.py

# API Endpoint
# http://127.0.0.1:5000/chat
🗨️ Example Usage

POST Request
{
    "message": "frustrated"
}
Response

{
    "persona": "General User",
    "response": "Okay, I understand you're feeling frustrated. I'm really sorry to hear that you're having trouble. Can you tell me a little bit more about what's going on? Knowing the specific issue will help me guide you towards the right solution.\n\nIs it perhaps related to logging in, payment, an API error, or managing your subscription? Don't worry, we'll figure this out together! Just let me know what's frustrating you, and I'll do my best to help."
}
