"""
Handles AI image analysis.
"""

import ollama
import os

def analyze_image(image_path, folders):
    """
    Sends an image to Ollama's vision model and asks it
    to classify the image into one of the available folders.
    """

    folder_names = [
        os.path.basename(folder)
        for folder in folders
    ]
    print("Analyzing...")
    response = ollama.chat(
        model="qwen2.5vl:7b",
        messages=[
            {
                "role": "user",
                "content": f"""
                    Identify the category in this image.
                    Only respond with these options. {folder_names}
                    If game cannot be identified, or is not in the options, respond with "unknown"
                    """,
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]

