from flask import Blueprint, jsonify
from database import get_history

history_bp = Blueprint("history", __name__)

@history_bp.route("/history", methods=["GET"])
def history():
    return jsonify(get_history())
