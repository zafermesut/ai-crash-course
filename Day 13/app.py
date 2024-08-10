import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('skin_cancer.h5')

def process_image(img):
    img = img.resize((170, 170))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

st.title('Skin Cancer Detection :cancer:')
st.write('Upload an image for skin cancer detection')
file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png', 'webp'])

if file is not None:
    img = Image.open(file)
    st.image(img, caption='Uploaded Image')
    image = process_image(img)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)

    class_names = ['Non_Cancer', 'Cancer']
    st.write(f'Prediction: {class_names[predicted_class]}')

