import streamlit as st
from config import pagesetup as ps


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

