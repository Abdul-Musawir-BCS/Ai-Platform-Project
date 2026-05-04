from flask import Blueprint, request, jsonify
import os

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    os.makedirs("static/uploads", exist_ok=True)

    path = f"static/uploads/{file.filename}"
    file.save(path)

    return jsonify({"path": path})
