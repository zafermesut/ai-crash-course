import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import streamlit as st

df = pd.read_excel('cars.xls')
x = df.drop('Price', axis=1)
y = df[['Price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Mileage', 'Cylinder', 'Liter', 'Doors']),
        ('cat', OneHotEncoder(), ['Make', 'Model', 'Trim', 'Type'])
    ]
)

model = LinearRegression()
pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', model)])
pipeline.fit(x_train, y_train)
pred = pipeline.predict(x_test)

rmse = mean_squared_error(pred, y_test) ** .5
r2 = r2_score(pred, y_test)

def price_pred(make, model, trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather):
    input_df = pd.DataFrame({
        'Make': [make],
        'Model': [model],
        'Trim': [trim],
        'Mileage': [mileage],
        'Type': [car_type],
        'Cylinder': [cylinder],
        'Liter': [liter],
        'Doors': [doors],
        'Cruise': [cruise],
        'Sound': [sound],
        'Leather': [leather]
    })
    
    prediction = pipeline.predict(input_df)[0]
    return prediction


st.title('MLOps - Car Price Prediction :red_car:')
st.write('Enter Car Details to get the Price Prediction')

def main():
    make = st.selectbox('Make', df['Make'].unique())
    model = st.selectbox('Model', df[df['Make'] == make]['Model'].unique())
    trim = st.selectbox('Trim', df[(df['Make'] == make) & (df['Model'] == model)]['Trim'].unique())
    mileage = st.number_input('Mileage', 200, 60000)
    car_type = st.selectbox('Type', df['Type'].unique())
    cylinder = st.selectbox('Cylinder', df['Cylinder'].unique())
    liter = st.number_input('Liter', 1,6)
    doors = st.selectbox('Doors', df['Doors'].unique())
    cruise = st.radio('Cruise',[0,1])
    sound = st.radio('Sound',[0,1])
    leather = st.radio('Leather',[0,1])
    if st.button('Predict'):
        price = price_pred(make, model, trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather)
        price = float(price)
        st.write(f'The predicted price is : ${price:.2f}')  

if __name__ == '__main__':
    main()



