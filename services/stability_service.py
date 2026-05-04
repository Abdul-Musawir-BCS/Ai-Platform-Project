import requests
import base64
from config import Config
from uuid import uuid4
import os

def generate_image(prompt):

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "Authorization": f"Bearer {Config.STABILITY_API_KEY}",
        "Accept": "image/*"
    }

    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise Exception(response.text)

    # Ensure folder exists
    os.makedirs("static/outputs", exist_ok=True)

    # Save image
    filename = f"{uuid4().hex}.png"
    path = f"static/outputs/{filename}"

    with open(path, "wb") as f:
        f.write(response.content)

    return path
