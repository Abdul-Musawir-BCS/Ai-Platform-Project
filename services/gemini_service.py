from google import genai
from config import Config

# Initialize Gemini client
client = genai.Client(api_key=Config.GEMINI_API_KEY)


# 🎨 Enhance Prompt
def enhance_prompt(prompt, mood):
    try:
        full_prompt = f"""
        You are an expert AI image prompt engineer.

        Improve the following prompt to be more detailed, vivid, and optimized for image generation.
        Add style, lighting, camera angles, and artistic detail.

        Mood: {mood}
        Base Prompt: {prompt}

        Return ONLY the improved prompt.
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=full_prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error enhancing prompt: {str(e)}"


# 💬 Chatbot / General AI
def chat_response(message):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=message
        )

        return response.text.strip()

    except Exception as e:
        return f"Chat error: {str(e)}"


# 🔍 Image Analysis (TEXT-BASED)
def analyze_image_text(image_path):
    try:
        prompt = f"""
        Analyze this image: {image_path}

        Provide:
        - Short summary
        - Objects detected
        - Image quality (clear, blurry, etc.)
        - A short creative story
        - A professional photographer's critique

        Keep it structured and clean.
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Analysis error: {str(e)}"


# 🧠 Prompt Suggestions
def suggest_improvements(prompt):
    try:
        suggestion_prompt = f"""
        Improve this image prompt and give 3 variations:

        Original: {prompt}

        Return:
        1. Cinematic version
        2. Artistic version
        3. Realistic version
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=suggestion_prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Suggestion error: {str(e)}"


# ⚖️ Compare Images
def compare_images_text(img1, img2):
    try:
        prompt = f"""
        Compare these two images:

        Image 1: {img1}
        Image 2: {img2}

        Provide:
        - Key differences
        - Quality comparison
        - Which is better and why
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Comparison error: {str(e)}"

