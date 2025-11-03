def detect_persona(user_message: str) -> str:
    msg = user_message.lower()
    if any(w in msg for w in ["angry", "upset", "frustrated", "not working"]):
        return "Frustrated User"
    elif any(w in msg for w in ["api", "endpoint", "server", "code", "error 500"]):
        return "Technical Expert"
    elif any(w in msg for w in ["report", "business", "client", "meeting"]):
        return "Business Executive"
    else:
        return "General User"