import streamlit as st
import pandas as pd

st.title('Getting data from form and writing to csv file :broken_heart:')

name = st.text_input('Name')
password = st.text_input('Password', type='password')
birth = st.date_input('Birth date')
age = st.slider('Age', 1, 100)
message = st.text_area('Message', max_chars=300, height=80)
if st.button('Submit'):
    ndf = pd.DataFrame({'Name': [name], 'Password': [password], 'Birth Date': [birth], 'Age': [age], 'Message': [message]})
    st.write(ndf)
    ndf.to_csv('data/user_data.csv', index=False)
    st.success('Data saved successfully')
st.divider()