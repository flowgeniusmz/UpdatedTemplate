import streamlit as st
from openai import OpenAI

def create_transcript(varAudioFile):

    client = OpenAI(api_key=st.secrets.openai.api_key)

    response = client.audio.transcriptions.create(
        model=st.secrets.openai.model_whisper,
        file=varAudioFile
    )

    transcript = response.text

    return transcript
