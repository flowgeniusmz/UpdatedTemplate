import streamlit as st
from openai import OpenAI
from audiorecorder import audiorecorder

def get_audio_recording():
# Add audio recorder
    audio = audiorecorder(
        start_prompt="Click to record", 
        stop_prompt="Click to stop recording"
    )

    if len(audio) > 0:
        # to play audio in frontend
        audio_playback = st.audio(audio.export().read())

        # to save audio to a file use pydub export method
        audio_file = audio.export(
            out_f="audio.wav",
            format="wav"
        )

        return audio_file

