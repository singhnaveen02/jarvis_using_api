import os
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyCYs92GaH18rtm5NsoWFMdrJo2qk2eN6qQ"))

st.set_page_config(page_title="Mini Jarvis 🤖", page_icon="🤖")
st.title("🤖 Mini Jarvis – Your Gemini-powered AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            reply = response.text
            st.markdown(reply)

    st.session_state.chat_history.append(("assistant", reply))
