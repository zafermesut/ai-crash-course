import streamlit as st
import google.generativeai as genai
from PIL import Image

#api_key = 'YOUR_API_KEY'
api_key = 'AIzaSyDNpp_u64U8mpeOmrpKrSUUOdptxyoxtQE'
genai.configure(api_key=api_key)

st.title('Analyze Image with Google Gemini')

model = genai.GenerativeModel('gemini-1.5-flash')
image = st.file_uploader('Upload Image:', type=['jpg', 'jpeg', 'png'])

if image is not None:
    img = Image.open(image)
    st.image(img)
    # response = model.generate_content(img)
    # st.write(response.parts[0])


question = st.text_input('Question:')
if st.button('Ask'):
    chat = model.start_chat(history=[])
    response = model.generate_content([question, img], stream = True)
    response.resolve()
    st.write(response.text)