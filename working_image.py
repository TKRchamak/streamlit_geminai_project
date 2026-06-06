import os
from dotenv import load_dotenv
from google import genai
import streamlit as st
from PIL import Image

load_dotenv()

apikey = os.getenv("GENAI_API_KEY")

client = genai.client.Client(api_key=apikey)

images = st.file_uploader(
        "Upload the photos of your notes",
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png"],
    )


if images:
    pil_images = []

    for image in images:
        img = Image.open(image)
        pil_images.append(img)    

    prompt_text = """summarized the image in note formate at max 100 words make sure to add
    necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt_text],
    )

    st.markdown(response.text)
