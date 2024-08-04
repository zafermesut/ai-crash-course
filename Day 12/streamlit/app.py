import streamlit as st
import pandas as pd
import plotly.express as px

st.title('MLops Streamlit Apps :flag-tr:')
menu = ['Home', 'About', 'Machine Learning', 'Deep Learning', 'Contact']
st.sidebar.selectbox('Menu', menu)

st.audio('data/song.mp3')
st.slider('Select a value', 1, 100)

df = pd.read_csv('data/prog_languages_data.csv')
fig = px.pie(df, values='Sum')
st.plotly_chart(fig)

fig2 = px.bar(df, x='lang', y='Sum')
st.plotly_chart(fig2)

file = st.file_uploader('Upload a file', type='csv')
st.code("""
        import pandas as pd
        df = read_csv('data/iris.csv')
        """)
st.success('Success')
st.error('Danger')
st.warning('Warning')
st.info('Info')


isim = st.text_input('Adınızı girin', max_chars=20)
# st.video('data/secret_of_success.mp4')
# st.camera_input('camera')

st.date_input('Date')
st.time_input('Time') 
st.text_input('Password', type='password')
st.text_area('Tell us a story', max_chars=200)
st.number_input('Age', 1,100)
st.radio("Marital status", ('married', 'single', 'widowed', 'engaged'))
st.selectbox("Programming languages ​​you know", ['Python', 'Java', 'C++', 'C#', 'Julia', 'Q#'])
st.multiselect("Programming languages ​​you know", ['Python', 'Java', 'C++', 'C#', 'Julia', 'Q#'])
st.image('data/image_01.jpg')
st.divider()

data = pd.read_csv('data/iris.csv')
st.write(data)

st.area_chart(data)
