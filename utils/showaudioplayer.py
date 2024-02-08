from io import BytesIO
from gtts import gTTS, gTTSError
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets.openai.api_key)
model_tts = st.secrets.openai.model_speech
voice_tts = st.secrets.openai.voice_speech
def show_audio_player(ai_content: str) -> None:
    sound_file = BytesIO()
    try:
        tts = 