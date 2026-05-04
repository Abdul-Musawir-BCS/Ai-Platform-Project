from flask import Blueprint, request, jsonify
from services.stability_service import generate_image

edit_bp = Blueprint("edit", __name__)

@edit_bp.route("/edit", methods=["POST"])
def edit():
    base = request.json.get("base_prompt")
    edit = request.json.get("edit_prompt")

    new_prompt = f"{base}, modified with: {edit}"

    image = generate_image(new_prompt)

    return jsonify({"image": image})
