from services.gemini_service import compare_images_text

def compare_images(img1, img2):
    """
    Compare two images using Gemini AI
    Give:
    - Differences
    - Quality comparison
    - Recommendation
    """
    return compare_images_text(img1, img2)

