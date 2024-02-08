import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=DeprecationWarning)

client = OpenAI(api_key=st.secrets.openai.api_key)

# Set variables

# Set session state

# Set functions

# Set Page Title
title = "FlowGenius"
subtitle = "Page3"
ps.set_title(varTitle=title, varSubtitle=subtitle)

# Set Page Overview
header = "Overview"
text = f"**{subtitle}** provides a....!"
ps.set_page_overview(varHeader=header, varText=text)




speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)

audio_file = speech_file_path
with open(audio_file, "rb") as f:
    audio_bytes = f.read()
    st.audio(audio_bytes)

