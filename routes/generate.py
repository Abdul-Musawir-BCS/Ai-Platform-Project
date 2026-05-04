from flask import Blueprint, request, jsonify
from services.gemini_service import enhance_prompt
from services.stability_service import generate_image
from database import save_image

generate_bp = Blueprint("generate", __name__)

@generate_bp.route("/generate", methods=["POST"])
def generate():
    data = request.json

    prompt = data.get("prompt")
    mood = data.get("mood")

    enhanced = enhance_prompt(prompt, mood)
    image_path = generate_image(enhanced)

    image_id = save_image(prompt, enhanced, image_path)

    return jsonify({
        "id": image_id,
        "image": image_path,
        "enhanced_prompt": enhanced
    })
