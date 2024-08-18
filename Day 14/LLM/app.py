import streamlit as st
import google.generativeai as genai

api_key = 'YOUR_API_KEY'
genai.configure(api_key=api_key)

st.title('Porsuk')

model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

question = st.text_input('Question:')
if st.button('Ask'):
    response = chat.send_message(question)
    st.write(response.text)
    st.write(chat.history)