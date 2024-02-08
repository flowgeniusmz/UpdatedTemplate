import streamlit as st
from config import pagesetup as ps
from functions import generateslides as gs


# Set variables

# Set session state

# Set functions

# Set Page Title
title = "FlowGenius"
subtitle = "Page1"
ps.set_title(varTitle=title, varSubtitle=subtitle)

# Set Page Overview
header = "Overview"
text = f"**{subtitle}** provides a....!"
ps.set_page_overview(varHeader=header, varText=text)

#Code
container1 = st.container()
with container1: 
    topic = st.text_input(
        label="PowerPoint Topic",
        key="input_ppt_topic"
    )
    btn_submit = st.button("Submit", key="btn_topic_submit")

    if btn_submit and topic:
        gs.generate_ppt_slides(topic)

