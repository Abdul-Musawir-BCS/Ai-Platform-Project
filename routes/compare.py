from flask import Blueprint, request, jsonify
from services.comparator import compare_images

compare_bp = Blueprint("compare", __name__)

@compare_bp.route("/compare", methods=["POST"])
def compare():
    img1 = request.json.get("img1")
    img2 = request.json.get("img2")

    result = compare_images(img1, img2)

    return jsonify({"result": result})
