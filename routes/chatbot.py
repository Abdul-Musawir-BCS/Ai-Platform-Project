from flask import Blueprint, request, jsonify
from services.gemini_service import chat_response

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")

    response = chat_response(message)

    return jsonify({"response": response})
