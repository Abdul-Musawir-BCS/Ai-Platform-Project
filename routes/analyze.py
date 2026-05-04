from flask import Blueprint, request, jsonify
from services.gemini_service import analyze_image_prompt
from PIL import Image
import io

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    try:
        # OPTION 1: uploaded file
        if 'file' in request.files:
            file = request.files['file']
            image = Image.open(io.BytesIO(file.read()))

        # OPTION 2: image path (generated image)
        else:
            data = request.get_json()
            image_path = data.get("image_path") if data else None

            if not image_path:
                return jsonify({"error": "No image provided"}), 400

            image = Image.open(image_path)

        prompt = """
        Analyze this image and provide:

        1. Short summary
        2. Objects detected
        3. Image quality (clear, blurry, lighting, etc.)
        4. Scene description
        5. A short creative story
        6. Photographer-style critique

        Keep it structured and clean.
        """

        result = analyze_image_prompt(prompt, image)

        return jsonify({"success": True, "analysis": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
