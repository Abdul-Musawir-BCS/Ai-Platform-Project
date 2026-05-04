from services.gemini_service import analyze_image_text

def analyze_image(image_path):
    """
    Takes image path and returns structured AI analysis.
    Provide: 
    - Short summary 
    - Objects detected 
    - Image quality 
    - Short creative story 
    """
    return analyze_image_text(image_path)
