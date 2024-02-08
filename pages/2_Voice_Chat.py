import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
from audio_recorder_streamlit import audio_recorder
from tempfile import NamedTemporaryFile
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set variables
client = OpenAI(api_key=st.secrets.openai.api_key)

# Set session state

# Set functions
def create_temp_file(varSuffix: str):
    with NamedTemporaryFile(delete=False, suffix=varSuffix) as tmp_file:
        tmp_file_path = tmp_file.name
        print(tmp_file_path)
    return tmp_file_path

def transcribe_audio(varAudioFilePath):
    with open(varAudioFilePath, "rb") as aud_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=aud_file
        )
        transcript_content = transcript.text
        print(transcript_content)
    return transcript_content

def save_audio_file(varAudioBytes, varFilePath):
    with open(varFilePath, "wb") as f:
        f.write(varAudioBytes)

def get_ai_response(varUserTranscript):
    messages = [
        {"role": "user", "content": varUserTranscript}
    ]
    response = client.chat.completions.create(
        model=st.secrets.openai.model_gpt4_preview,
        messages=messages
    )
    content = response.choices[0].message.content
    return content

def create_ai_voice_file(varSpeech):
    speech_file_path = create_temp_file(".mp3")
    response = client.audio.speech.create(
        model=st.secrets.openai.model_speech,
        voice=st.secrets.openai.voice_speech,
        input=varSpeech
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path

# Set Page Title
title = "FlowGenius"
subtitle = "Voice Chat"
ps.set_title(varTitle=title, varSubtitle=subtitle)

# Set Page Overview
header = "Overview"
text = f"**{subtitle}** provides a....!"
ps.set_page_overview(varHeader=header, varText=text)

# Get Audio Recording
container1 = st.container()
container2 = st.empty()
with container1:
    ps.set_blue_header("User Input")
    audio_user_bytes = audio_recorder()

    if audio_user_bytes:
        st.audio(audio_user_bytes, format="audio/wav")
        audio_user_file_path = create_temp_file(".mp3")
        save_audio_file(audio_user_bytes, audio_user_file_path)
        audio_user_transcript = transcribe_audio(audio_user_file_path)
        if audio_user_transcript:
            ps.set_blue_header("User Transcript")
            exp1 = st.expander("User Transcript", expanded=True)
            with exp1:
                st.markdown(audio_user_transcript)


        audio_ai_text = get_ai_response(audio_user_transcript)
        ai_voice_path = create_ai_voice_file(audio_ai_text)
        with open(ai_voice_path, "rb") as fpath:
            ai_voice_bytes = fpath.read()
            st.audio(ai_voice_bytes)
        

        

