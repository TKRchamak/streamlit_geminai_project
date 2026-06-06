from gtts import gTTS
import stremalit as st
import io

text = "Hello, how are you?"

speech = gTTS(text, lang='en', slow=False)
audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer.getvalue())