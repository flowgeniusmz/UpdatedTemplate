import streamlit as st
from openai import OpenAI
import warnings
from pathlib import Path
from functions import tempfile as tf
from utils import showwidgets as wid

client = OpenAI(api_key=st.secrets.openai.api_key)

def get_speech_text(varTranscript):

    messages = [
        {"role": "user", "content": varTranscript}
    ]

    response = client.chat.completions.create(
        model=st.secrets.openai.model_gpt4_preview,
        messages=messages
    )

    content = response.choices[0].message.content

    return content


def get_speech_voice_filepath(varResponseSpeech):
    speech_file_path = tf.create_temp_file(".mp3")

    response = client.audio.speech.create(
        model=st.secrets.openai.model_speech,
        voice=st.secrets.openai.voice_speech,
        input=varResponseSpeech
    )

    response.stream_to_file(speech_file_path)
    return speech_file_path

def create_speech(varTranscript):
    speech_text = get_speech_text(varTranscript)
    speech_voice_file = get_speech_voice_filepath(speech_text)
    wid.play_openai_speech(speech_voice_file)
    return speech_text



#speech_file_path = Path(__file__).parent / "speech.mp3"
#response = client.audio.speech.create(
#  model="tts-1",
#  voice="alloy",
#  input="The quick brown fox jumped over the lazy dog."
#)
#response.stream_to_file(speech_file_path)

#audio_file = speech_file_path
#with open(audio_file, "rb") as f:
#    audio_bytes = f.read()
#    st.audio(audio_bytes)