from google import genai
from dotenv import load_dotenv
import os 
from gtts import gTTS
import io

load_dotenv()

apikey = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=apikey)

def note_generator(images):
    prompt = """summarized the image in note formate at max 100 words make sure to add 
    necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images, prompt]
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(images, difficulty):
    prompt = f"""Generate a quiz based on the content of the image with {difficulty} level difficulty.
    The quiz should consist of 3 questions, each with 4 multiple-choice answers. also include the correct answer"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images, prompt]
    )

    return response.text