🤖 Persona-Adaptive Customer Support Agent

An intelligent AI-powered support agent that dynamically adapts its responses based on the customer’s persona —
such as Frustrated User, Technical Expert, or Business Executive.

It leverages LangChain, OpenAI LLMs, and a Chroma Vector Database to deliver context-aware, emotionally adaptive, and persona-aligned responses for smarter customer interactions.

🚀 Project Overview
🎯 Goal

To build a Customer Support Chatbot that can:

🧠 Detect the user’s persona — analyze tone, sentiment, and technical depth of queries.

📚 Retrieve relevant knowledge base (KB) content using semantic search.

🗣️ Adapt its response tone and style based on persona (empathetic, formal, or technical).

🔄 Escalate unresolved or critical issues to human agents with full conversation context.

🧩 Tech Stack
Component	Technology
Framework	Flask, LangChain
LLM Model	OpenAI GPT (or Gemini alternative)
Vector Store	ChromaDB
Programming Language	Python
Environment	dotenv
Persona Logic	JSON / Rule-based Detection
⚙️ Key Features

✅ Persona Detection: Uses tone and intent analysis to categorize users (e.g., Frustrated, Business, Technical).
📚 Knowledge Retrieval: Employs Chroma for semantic document retrieval from the knowledge base.
🗣️ Adaptive Response: Adjusts tone and complexity according to persona.
🔄 Contextual Escalation: Hands off issues to human agents with summarized context.
💬 Emotion Awareness: Embeds empathy and understanding in responses for better user satisfaction.

🧱 Architecture
User Query
   ↓
Persona Detection (Sentiment + Intent)
   ↓
Knowledge Retrieval (Chroma Vector Search)
   ↓
Adaptive Response Generation (LLM)
   ↓
Context Handoff / Reply

⚡ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/persona-adaptive-support-agent.git
cd persona-adaptive-support-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add API Key

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here

4️⃣ Run the Application
python app.py

🧠 Example Workflow

Input:

“I’ve tried resetting my account three times, and it still doesn’t work!”

Detected Persona: Frustrated User 😤
Retrieved Info: Account recovery steps from KB
Response Tone: Empathetic and calming

Bot Reply:

“I completely understand how frustrating this can be. Let’s fix this together — please try these recovery steps below 👇”

🔮 Future Enhancements

🧩 Integrate multi-turn conversation memory

🌐 Add a Streamlit or React web UI

🎭 Train persona classification model using fine-tuned embeddings

🧠 Use Gemini 1.5 Pro for emotion-aware generative responses

👨‍💻 Author

Chandan Kumar Gupta
AI/ML Engineer | LangChain & GenAI Developer
🔗 LinkedIn
 • GitHub
