# UTILITIES (UTILS)

## Clear Chat (clearchat.py)
- Clears the chat session state variables by resetting them to null values or blank arrays
- Includes st.session_state.generated, past, messages, user_text
- clearchat.clear_chat()
- Packages: streamlit

## Show Widgets (showwidgets.py)
- Contains functions that display certain streamlit widgets
- show_text_input()
- show_chat_buttons()
- Packages: streamlit, streamlit-chat

## Show Chat (showchat.py)
- Contains functions to display chat
- Uses native streamlit chat and custom streamlit-chat package
