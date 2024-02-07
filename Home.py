import streamlit as st
from config import pagesetup as ps

# Set page config
st.set_page_config(page_title="FlowGenius", layout="wide", initial_sidebar_state="collapsed")

# Set variables

# Set session state

# Set functions

# Set Page Title
title = "FlowGenius"
subtitle = "Home"
ps.set_title(varTitle=title, varSubtitle=subtitle)

# Set Page Overview
header = "Overview"
text = f"**{subtitle}** provides a....!"
ps.set_page_overview(varHeader=header, varText=text)

