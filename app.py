
import streamlit as st
from api_calling import audio_transcription, note_generator, quiz_generator
from PIL import Image

# title
st.title("My Streamlit App with GenAI")
st.markdown(
    "This is a simple Streamlit app that integrates GenAI for generating content."
)
st.divider()

with st.sidebar:
    st.header("Sidebar")
    images = st.file_uploader(
        "Upload the photos of your notes",
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png"],
    )

    if images:
        if len(images) > 3:
            st.error("Please upload a maximum of 3 images.")
        else:
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    # difficulty 
    selected_difficulty = st.selectbox(
        "Select difficulty:",
        ("Easy", "Medium", "Hard"),
        index=None,
    )

    pressed = st.button("Click the button to initial AI", type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image.")
    if not selected_difficulty:
        st.error("Please select a difficulty level.")

    if images and selected_difficulty:
        # note
        pil_images = []

        for image in images:
            img = Image.open(image)
            pil_images.append(img)    
        
        with st.container(border=True):
            st.subheader("Your Notes")
            with st.spinner("Generating notes for you ..."):
                note = note_generator(pil_images)
                st.text(note)

        # audio output
        with st.container(border=True):
            st.subheader("Auto Transcription")
            with st.spinner("Generating audio for you ..."):

                generated_notes = note.replace("*", "")
                generated_notes = note.replace("#", "")
                generated_notes = note.replace("-", "")
                generated_notes = note.replace("`", "")
                audio_buffer = audio_transcription(generated_notes)
                st.audio(audio_buffer.getvalue())

        # quiz
        with st.container(border=True): 
            st.subheader("Generated Quiz")
            with st.spinner("Generating quiz for you ..."):
                quiz = quiz_generator(pil_images, selected_difficulty)
                st.markdown(quiz)
