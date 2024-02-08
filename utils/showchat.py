import streamlit as st
from streamlit_chat import message

def show_chat_st(ai_content: str, user_text: str) -> None:
    if ai_content not in st.session_state.generated:
        #store the ai content
        st.session_state.past.append(user_text)
        st.session_state.generated.append(ai_content)
    if st.session_state.generated:
        generated_length = len(st.session_state.generated)
        for i in range(generated_length):
            msg = st.session_state.past[i]
            msg_role = msg['role']
            msg_content = msg['content']
            with st.chat_message(msg_role):
                st.markdown(msg_content)
            