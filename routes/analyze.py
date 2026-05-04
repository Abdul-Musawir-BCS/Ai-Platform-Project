from flask import Blueprint, request, jsonify
from google import genai
from PIL import Image
import io
import os

analyze_bp = Blueprint("analyze", __name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    try:
        # OPTION 1: uploaded file
        if 'file' in request.files:
            file = request.files['file']
            image = Image.open(io.BytesIO(file.read()))

        # OPTION 2: image path (generated image)
        else:
            image_path = request.json.get("image_path")
            if not image_path:
                return jsonify({"error": "No image provided"}), 400

            image = Image.open(image_path)

        prompt = """
        Analyze this image in structured format:

        1. Caption
        2. Summary
        3. Key objects detected
        4. Mood
        5. Scene type
        6. Image quality (sharp/blurry/etc)
        7. Creative short story
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=[prompt, image]
        )

        return jsonify({"analysis": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
