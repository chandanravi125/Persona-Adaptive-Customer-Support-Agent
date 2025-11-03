# app.py
from flask import Flask, request, jsonify
from persona_detector import detect_persona
from rag_retriever import get_relevant_docs
from response_generator import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the Persona Agent API!"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        user_query = data.get("message", "")
        if not user_query:
            return jsonify({"error": "Message required"}), 400
        persona = detect_persona(user_query)
        kb_docs = get_relevant_docs(user_query)
        ai_reply = generate_response(persona, user_query, kb_docs)
        return jsonify({
            "persona": persona,
            "response": ai_reply
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)