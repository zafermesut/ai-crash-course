import streamlit as st
import pandas as pd
import pickle

st.title('Model that Predict Salary by Experience, Test, Interview :heavy_dollar_sign:')
model = pickle.load(open('data/salary.pkl', 'rb'))

exp = st.number_input('Experience', 0, 10)
test = st.number_input('Test', 0, 10)
interview = st.number_input('Interview', 0, 10)
if st.button('Predict'):
    prediction = model.predict([[exp, test, interview]])
    prediction = round(prediction[0][0], 2)
    st.success(f'Predicted Salary is {prediction} $')